import requests
import pandas as pd
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm

# Load all IMDb TSV files and treat '\\N' as NaN
# low_memory=False to prevent type inference issues with large datasets
name_basics = pd.read_csv('name.basics.tsv', sep='\t', na_values='\\N', low_memory=False)
title_akas = pd.read_csv('title.akas.tsv', sep='\t', na_values='\\N', low_memory=False)
title_basics = pd.read_csv('title.basics.tsv', sep='\t', na_values='\\N', low_memory=False)
title_crew = pd.read_csv('title.crew.tsv', sep='\t', na_values='\\N', low_memory=False)
title_ratings = pd.read_csv('title.ratings.tsv', sep='\t', na_values='\\N', low_memory=False)
title_principals = pd.read_csv('title.principals.tsv', sep='\t', na_values='\\N', low_memory=False)

# Filter only movie records and merge ratings and directors info
movies = title_basics[title_basics['titleType'] == 'movie']
movies = movies.merge(title_ratings, on='tconst', how='left')
movies = movies.merge(title_crew[['tconst', 'directors']], on='tconst', how='left')
movies['directorId'] = movies['directors'].str.split(',').str[0]
movies = movies.merge(name_basics[['nconst', 'primaryName']], left_on='directorId', right_on='nconst', how='left')
movies.rename(columns={'primaryName': 'director'}, inplace=True)

# Drop rows with missing critical data
movies.dropna(subset=['primaryTitle', 'genres', 'averageRating'], inplace=True)

# Load Rotten Tomatoes reviews and clean it
rt = pd.read_csv('rotten_tomatoes_movie_reviews.csv')
rt = rt[rt['reviewState'].isin(['fresh', 'rotten'])]
rt.dropna(subset=['scoreSentiment'], inplace=True)

# Convert review scores to normalized floats (e.g., 3.5/4 -> 0.875)
def convert_score(score):
    try:
        parts = score.split('/')
        return float(parts[0]) / float(parts[1])
    except:
        return None

rt['originalScoreNum'] = rt['originalScore'].apply(convert_score)
rt['isFresh'] = rt['reviewState'].map({'fresh': 1, 'rotten': 0})
rt['sentimentLabel'] = rt['scoreSentiment'].map({'POSITIVE': 1, 'NEGATIVE': -1})
rt['isTopCritic'] = rt['isTopCritic'].astype(bool)
rt['creationDate'] = pd.to_datetime(rt['creationDate'], errors='coerce')

# Aggregate Rotten Tomatoes data by movie ID
rt_grouped = rt.groupby('id').agg({
    'sentimentLabel': 'mean',
    'isTopCritic': 'mean',
    'originalScoreNum': 'mean',
    'isFresh': 'mean'
}).reset_index()

# Normalize movie titles for accurate merging
def normalize_title(title):
    if pd.isna(title): return ""
    return title.strip().lower().replace("’", "'").replace(":", "").replace("-", " ").replace("_", " ")

movies['normalizedTitle'] = movies['primaryTitle'].apply(normalize_title)
rt_grouped['normalizedTitle'] = rt_grouped['id'].apply(normalize_title)

# Merge IMDb and RT data on normalized title
full_df = movies.merge(rt_grouped, on='normalizedTitle', how='inner')
full_df.dropna(subset=['averageRating', 'sentimentLabel', 'genres', 'director'], inplace=True)
full_df['genres_list'] = full_df['genres'].str.split(',')

# Drop duplicates based on title and release year, and keep only movies since 1995
full_df['releaseYear'] = pd.to_numeric(full_df['startYear'], errors='coerce')
full_df.drop_duplicates(subset=['primaryTitle', 'releaseYear'], inplace=True)
full_df = full_df[full_df['releaseYear'] >= 1995]

# TMDb API setup
TMDB_API_KEY = "17559fd680a786c2d00d55114cc9c081"
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_DETAILS_URL = "https://api.themoviedb.org/3/movie/{}"

# Configure requests session with retry strategy
session = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=100, pool_maxsize=100)
session.mount("https://", adapter)
session.mount("http://", adapter)

# Initialize new columns for TMDb data
full_df['tmdb_budget'] = None
full_df['tmdb_revenue'] = None

# TMDb helper functions
def get_tmdb_id(title, year):
    try:
        params = {"api_key": TMDB_API_KEY, "query": title, "year": int(float(year)) if pd.notna(year) else None}
        response = session.get(TMDB_SEARCH_URL, params=params, timeout=8)
        data = response.json()
        if data['results']:
            return data['results'][0]['id']
    except:
        return None

def get_tmdb_details(tmdb_id):
    try:
        url = TMDB_DETAILS_URL.format(tmdb_id)
        response = session.get(url, params={"api_key": TMDB_API_KEY}, timeout=8)
        data = response.json()
        return data.get('budget'), data.get('revenue')
    except:
        return None, None

def fetch_movie_data(index, title, year):
    tmdb_id = get_tmdb_id(title, year)
    if tmdb_id:
        budget, revenue = get_tmdb_details(tmdb_id)
        if budget and revenue:
            return index, budget, revenue
    return index, None, None

# Run scraping in parallel threads and checkpoint periodically, max 75 workers in order to gain speed
checkpoint_path = "tmdb_checkpoint.csv"
try:
    with ThreadPoolExecutor(max_workers=75) as executor:
        futures = {
            executor.submit(fetch_movie_data, idx, row['primaryTitle'], row['releaseYear']): idx
            for idx, row in full_df.iterrows()
            if pd.isna(row['tmdb_budget']) or pd.isna(row['tmdb_revenue'])
        }
        for i, future in enumerate(tqdm(as_completed(futures), total=len(futures))):
            try:
                idx, budget, revenue = future.result()
                if budget is not None and revenue is not None:
                    full_df.at[idx, 'tmdb_budget'] = budget
                    full_df.at[idx, 'tmdb_revenue'] = revenue
                if (i + 1) % 50 == 0:
                    print(f"Checkpoint at movie {i+1}")
                    full_df.to_csv(checkpoint_path, index=False)
                    print(full_df[['primaryTitle', 'releaseYear', 'tmdb_budget', 'tmdb_revenue']].dropna().tail(5))
            except Exception as e:
                print(f"Error at row {i}: {e}")
except KeyboardInterrupt:
    full_df.to_csv(checkpoint_path, index=False)
    raise

# Final data cleanup and export
full_df.dropna(subset=['tmdb_budget', 'tmdb_revenue'], inplace=True)
full_df = full_df[full_df['releaseYear'] >= 1990]
full_df['tmdb_profit'] = full_df['tmdb_revenue'] - full_df['tmdb_budget']
full_df.to_csv("full_df_with_tmdb_profit.csv", index=False)

# Drop unused columns to clean final dataset
full_df.drop(columns=['titleType', 'isAdult', 'endYear'], inplace=True)

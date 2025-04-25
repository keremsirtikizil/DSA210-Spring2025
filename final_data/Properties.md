## 📄 Dataset Description — `full_df_with_tmdb_profit.csv`

This dataset integrates **IMDb**, **Rotten Tomatoes**, and **TMDb API** data for over **4,000 movies** released since 1995. It combines detailed metadata, director info, critic sentiment, runtime, and financial information (budget, revenue, profit) for comprehensive exploratory and statistical analysis.

---

### Core Movie Info

| Column | Description |
|--------|-------------|
| `tconst` | Unique IMDb movie ID (e.g., `tt1234567`) |
| `primaryTitle` | Official title of the movie |
| `originalTitle` | Original language title |
| `startYear` / `releaseYear` | Year the movie was released |
| `runtimeMinutes` | Duration of the film in minutes |
| `genres` / `genres_list` | List of movie genres (Action, Drama, etc.) |

---

### Director Information

| Column | Description |
|--------|-------------|
| `directors` | IMDb IDs of directors (can be multiple) |
| `directorId` | First (primary) director's IMDb ID |
| `director` | Full name of the main director |

---

### IMDb Ratings

| Column | Description |
|--------|-------------|
| `averageRating` | IMDb user score (0–10) |
| `numVotes` | Number of IMDb votes received |
| `rating_group` | Grouped rating categories (e.g., 6–7, 7–8) |

---

### Rotten Tomatoes (RT) Metrics

| Column | Description |
|--------|-------------|
| `id` | Rotten Tomatoes movie ID |
| `sentimentLabel` | Average sentiment polarity (1 = Positive, -1 = Negative) |
| `isTopCritic` | Ratio of top critic reviews |
| `originalScoreNum` | Normalized RT review score (0 to 1 scale) |
| `isFresh` | Proportion of 'fresh' reviews |



---

### TMDb Financials

| Column | Description |
|--------|-------------|
| `tmdb_budget` | Movie production budget (USD) |
| `tmdb_revenue` | Total worldwide box office revenue (USD) |
| `tmdb_profit` | Revenue minus budget (USD) |

---

### Utility & Engineered Features

| Column | Description |
|--------|-------------|
| `normalizedTitle` | Simplified lowercase movie title used for joining datasets |

---

### Final Cleaning Summary

- All rows with **missing values** (`NaN`) have been removed
- Final DataFrame dimensions:
  - **Rows:** 4,096 movies
  - **Columns:** 29 attributes

---


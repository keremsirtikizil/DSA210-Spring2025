**DSA210-Spring2025**

# DSA210 PROJECT

**Project: Analyzing the Influence of Movie Attributes on Box Office Success**

## **Overview**
The film industry is a high-stakes market where financial success depends on multiple factors, including budget, genre, director reputation, and audience reception. However, it remains unclear which attributes contribute the most to a film’s box office revenue. This project aims to analyze the relationship between various movie attributes and their commercial success using publicly available datasets from IMDb, Rotten Tomatoes, and Box Office Mojo. By leveraging statistical analysis and machine learning models, this study will identify key predictors of box office performance and assess whether certain combinations of attributes consistently lead to higher revenue.

## **Motivation**
The entertainment industry continues to evolve, with streaming services and changing audience preferences impacting traditional box office trends. Understanding what drives box office success is crucial for production studios, investors, and marketers. This study seeks to answer:

- Does a larger production budget always translate to higher revenue?
- Do certain genres or genre combinations (e.g., Action + Sci-Fi) perform better?
- Does a well-known director significantly boost box office performance?
- How do audience ratings (e.g., IMDb, Rotten Tomatoes) correlate with financial success?

By systematically analyzing these questions, this project will provide empirical insights into how different movie characteristics influence box office earnings.

## **Data Sources**
The datasets for this study will be obtained from the following sources:

- **IMDb Datasets** (https://datasets.imdbws.com)
  - Movie metadata, including titles, genres, directors, and user ratings.
  - Available in TSV format.
- **Rotten Tomatoes Datasets**
  - Audience and critic scores for movies.
  - May require web scraping or API access.
- **Box Office Datasets** (Box Office Mojo, The Numbers)
  - Box office performance, including domestic and international earnings.
  - Data extraction may require web scraping or API access.

## **Methodology**

### **Data Collection & Cleaning**
- Extract movie attributes from IMDb, Rotten Tomatoes, and Box Office Mojo.
- Handle missing values and ensure consistency in budget and revenue figures.
- Convert categorical variables (e.g., genre encoding, director reputation scores) for analysis.

### **Exploratory Data Analysis (EDA)**
- Visualize trends in budget, genre popularity, and revenue distribution.
- Identify correlations between movie attributes and box office success.

### **Statistical Analysis & Hypothesis Testing**
- Conduct hypothesis testing (T-tests, ANOVA) to determine significant relationships.
- Examine the impact of budget, genre, and director reputation on revenue.
- Test whether highly-rated movies consistently generate more revenue.

### **Machine Learning Modeling**
- **Regression Analysis:** Quantify relationships between budget, genre, and box office earnings.
- **Clustering:** Group movies based on success metrics and key attributes.
- **Predictive Modeling:** Develop machine learning models (Random Forest, XGBoost) to predict box office revenue based on pre-release factors.

## **Data Collection Plan**
- Gather and clean IMDb, Rotten Tomatoes, and Box Office datasets.
- Validate and preprocess the data to ensure accuracy.
- Conduct initial EDA before moving to statistical analysis and modeling.
- Analyze trends in movie success over different time periods.

## **Findings**

### **Exploratory Data Analysis**

#### Insight 1
- This histogram shows the distribution of movie profits (tmdb_profit). The data is highly right-skewed, with the majority of films generating little to no profit or even losses. Only a small minority of movies reach exceptionally high profit levels (e.g., $500M+), which suggests outliers and motivates the later use of log-transformation during modeling.

<img width="938" alt="Screenshot 2025-05-20 at 00 25 14" src="https://github.com/user-attachments/assets/0befcf5e-be4d-4de0-ab0c-7b00b930e688" />

#### Insight 2
- This scatter plot visualizes the relationship between a movie’s production budget and its resulting profit. While a loose upward trend is present — suggesting that higher investments can lead to higher returns — there is also substantial variance. Several high-budget movies still fail to return profit, revealing that budget alone does not guarantee success.
<img width="944" alt="Screenshot 2025-05-20 at 00 33 02" src="https://github.com/user-attachments/assets/b86d5af1-8c9b-4ad0-9db8-0c67e27855b4" />

#### Insight 3
- This heatmap summarizes pairwise correlations among key numerical features. Unsurprisingly, tmdb_budget and tmdb_revenue are highly correlated. However, tmdb_profit shows a weaker relationship with other variables like averageRating and numVotes, indicating that movie success is multifactorial and not easily predicted by a single metric.
<img width="950" alt="Screenshot 2025-05-20 at 00 35 00" src="https://github.com/user-attachments/assets/091d2875-446d-492f-a0d5-6023433b67b5" />

#### Insight 4
- This bar chart compares the average profits of the most frequently appearing directors in the dataset. Certain directors consistently deliver profitable films, while others vary widely. This plot supports the hypothesis that director reputation or prior success can be used as a predictive feature for financial performance.
<img width="935" alt="Screenshot 2025-05-20 at 00 21 52" src="https://github.com/user-attachments/assets/abbb7a48-ed50-49cc-9874-9123e9c5e8a1" />

#### Insight 5
- This boxplot compares the distribution of profits for movies categorized by IMDb rating group (low, mid, high). As expected, higher-rated films tend to earn more profit on average, though the variance is high. Some low-rated films are surprisingly profitable, suggesting that commercial success and audience perception are not always aligned.
<img width="959" alt="Screenshot 2025-05-20 at 00 48 14" src="https://github.com/user-attachments/assets/51ab6df4-0077-4210-91ab-587997ed1a3e" />

#### Insight 6
- This histogram shows that IMDb ratings (averageRating) mostly fall between 5 and 8. The distribution is bell-shaped, supporting the later decision to categorize movies into low, mid, and high quality groups for classification purposes.
<img width="948" alt="Screenshot 2025-05-20 at 00 50 25" src="https://github.com/user-attachments/assets/5633c38b-1331-456a-8c09-ab4ca62b6b96" />

#### Insight 7
- This boxplot shows the IMDb rating distributions for the top 8 most frequent directors in the dataset. Directors like Steven Spielberg and Clint Eastwood have consistently high ratings with low variability, while others like Robert Rodriguez show a wider spread in audience reception. Overall, it highlights how some directors maintain a more reliable level of critical success than others.
<img width="942" alt="Screenshot 2025-05-20 at 00 55 06" src="https://github.com/user-attachments/assets/f5aab76a-22d5-48b5-ab82-d6e6b7b62037" />


- Please go to [EDA.ipnyb](https://github.com/keremsirtikizil/DSA210-Spring2025/blob/main/EDA/EDA.ipynb) file to see more insights about my dataset.

### **Hypothesis Testing**

- will cont.

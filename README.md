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

<br>

### **Hypothesis Testing**

#### **Hypothesis 1**
**Production Budget and Revenue Relationship**
- H₀ (Null): There is no relationship between production budget and revenue (the slope of the regression line is zero).
- H₁ (Alternative): There is a positive relationship between production budget and revenue.
**Methodology:**
- A simple linear regression was conducted to assess the relationship between a movie's budget and its revenue. The regression line’s slope and the coefficient of determination (R²) were examined. Additionally, a t-test was performed to determine if the slope is significantly different from zero.

**Results**
- R² value: 0.251 (indicating around 25% of revenue variability can be explained by budget)
- Slope: 1.175 (positive)
- p-value: < 0.0001 (highly significant)

**Interpretation**
- The null hypothesis was rejected, indicating a statistically significant positive relationship between budget and revenue. While budget is a significant predictor, the modest R² suggests other factors also influence revenue.
<img width="649" alt="Screenshot 2025-05-27 at 10 17 16" src="https://github.com/user-attachments/assets/d6379763-45ca-46c3-aef5-79557b134fec" />

#### **Hypothesis 2**
**Revenue Differences Across Genres**
- H₀ (Null): Average revenue is the same across different genres/genre combinations.
- H₁ (Alternative): At least one genre has a different average revenue.
**Methodology**
- An ANOVA (F-test) was conducted to compare average revenues across unique genre combinations. A bar chart was also generated to visualize average revenue for a sample of genres.

**Results**
- F-statistic: 1.567
- p-value: < 0.0001 (highly significant)

**Interpretation**
- The null hypothesis was rejected. This indicates significant differences in average revenue across genres, suggesting that some genres (or genre combinations) tend to perform better financially than others.
<img width="945" alt="Screenshot 2025-05-27 at 10 17 29" src="https://github.com/user-attachments/assets/3218dbab-1fe2-429d-8725-10d61414dc6c" />

#### **Hypothesis 3**
**Correlation Between Runtime and Revenue**
- H₀ (Null): There is no correlation between runtime and revenue.
- H₁ (Alternative): There is a correlation between runtime and revenue.
**Methodology**
- A Pearson correlation test was performed to evaluate the linear relationship between runtime and revenue. Logarithmic scales were used in scatterplots for visualization due to the skewed data.

**Results**
- Correlation coefficient: 0.089
- p-value: < 0.0001 (significant)

**Interpretation**
- The null hypothesis was rejected. However, the correlation coefficient is very weak, indicating that while there is a statistically significant correlation, runtime is not a strong predictor of revenue on its own.
<img width="961" alt="Screenshot 2025-05-27 at 10 17 43" src="https://github.com/user-attachments/assets/b8d8bc62-7aa8-4a9b-a518-548acd3f47cd" />

#### **Hypothesis 4**
**Correlation Between Audience Ratings and Profit**
- H₀ (Null): There is no correlation between ratings (IMDb, Rotten Tomatoes) and profit.
- H₁ (Alternative): There is a correlation between ratings and profit.
**Methodology**
Two tests were conducted:
- Spearman rank correlation for IMDb ratings (continuous) vs. log-transformed profit.
- Point-biserial correlation for Rotten Tomatoes “freshness” (binary) vs. log-transformed profit.
- Scatterplots were created for visual reference.

**Results**

IMDb Rating vs. Profit:
- Spearman r: 0.036
- p-value: 0.138 (not significant)

Rotten Tomatoes Freshness vs. Profit:
- Point-biserial r: -0.013
- p-value: 0.596 (not significant)

**Interpretation**
- For both tests, the null hypothesis was not rejected. This suggests no significant correlation between audience ratings and financial success in the dataset analyzed.
<img width="952" alt="Screenshot 2025-05-27 at 10 17 51" src="https://github.com/user-attachments/assets/e34c43e0-94e7-40b7-81c3-368b0b07bdc8" />


### **Machine Learning**

**Regression: Predicting TMDb Revenue**

Objective:
- The goal of this analysis was to build predictive models to estimate a movie's TMDb revenue based on available features, including budget, ratings, votes, genres, and temporal information. By evaluating multiple regression algorithms, we aimed to understand which model best captures the underlying patterns in the data and to assess the impact of different features on financial outcomes.
 

To enhance model performance and handle skewed data (Feature Engineering):
- Log-transformations were applied to tmdb_budget and numVotes (log_budget, log_votes) to reduce skewness.
- A decade feature was created from releaseYear to capture temporal trends.
- num_genres was added to represent genre diversity.
- Genres were one-hot encoded using MultiLabelBinarizer to transform multi-label genre data into binary indicator columns (e.g., Action, Comedy, etc.).
- Missing values in numerical columns were imputed using mean values, while categorical columns (if any) were filled using mode values.

**Model Training and Evaluation**

Three regression models were trained and evaluated:
- Random Forest Regressor
- Linear Regression
- Gradient Boosting Regressor
- (The dataset was split into an 80% training set and a 20% test set using train_test_split.)

Performance metrics used for evaluation:
- Root Mean Squared Error (RMSE): Measures average prediction error magnitude.
- R² Score: Indicates how well the model explains variance in the target variable (tmdb_revenue).

**Results**

| Model                | RMSE (USD)      | R² Score |
|----------------------|-----------------|-----------|
| Random Forest        | **111,167,000** | **0.583** |
| Linear Regression    | 148,970,000     | 0.251     |
| Gradient Boosting    | 112,522,000     | 0.573     |


**Interpretation & Insights**

Random Forest Regressor:
- Achieved the lowest RMSE and highest R² among the models.
- Captured complex, non-linear relationships between features and revenue, handling feature interactions without explicit specification.
- R² of 0.583 suggests that ~58% of revenue variability can be explained by the features used. This indicates a moderate predictive power, but also highlights the influence of unmodeled factors (e.g., marketing, competition, global events).

Linear Regression:
- Performance was substantially lower than the tree-based models, with an R² of 0.251.
- The model assumes a strictly linear relationship between features and revenue, which likely oversimplifies the dynamics of movie performance.
- Linear regression may struggle with feature interactions and non-linear patterns present in the dataset.

Gradient Boosting Regressor:
- Performed almost as well as Random Forest, with a slightly higher RMSE and a slightly lower R².
- Gradient Boosting, being a sequential ensemble method, likely captured complex relationships but was marginally less effective in this context compared to Random Forest, possibly due to the limited tuning (default hyperparameters).

**Conclusion** 
- The Random Forest Regressor outperformed other models and appears to be the best choice for predicting TMDb revenue using the available dataset.
- However, the R² scores below 0.6 for all models indicate that a large portion of revenue variability remains unexplained. This suggests that while the models can provide reasonable estimates, external factors (e.g., marketing, distribution, competition, critical reviews) significantly influence movie revenue and were not captured in this dataset.
<img width="680" alt="Screenshot 2025-05-27 at 10 47 52" src="https://github.com/user-attachments/assets/e3ed066d-19de-4634-a7b6-8ef8ab4548d1" />

**Recommendations for Further Work**
- Feature Expansion: Include variables such as marketing spend, release date (seasonality), franchise status (sequel, prequel), and star power.
- Hyperparameter Tuning: Conduct grid or random search for optimal parameters, especially for tree-based models.
- Modeling Techniques: Explore more (advanced) models like XGBoost or LightGBM and consider neural networks for capturing deeper patterns.
- Residual Analysis: Investigate model residuals to identify systematic errors or patterns.

<br><br>

**Classification Modeling: Predicting IMDb Rating Group ("Low", "Mid", "High")**

Objective:
- This classification task aimed to predict a movie’s IMDb rating group—categorized as low (<6.0), mid (6.0–7.5), or high (>7.5)—based on features known before release, such as budget, votes, genre, and temporal information. This can help studios make informed decisions in pre-production and marketing phases by estimating a movie’s potential reception.

The dataset included:
- Target Variable: rating_group (low, mid, high)
- Features: Log-transformed budget and votes, original score, freshness indicator, decade of release, number of genres, and genre dummy variables.
- Missing values were imputed with mean (numerical) or mode (categorical).
- The dataset was split into an 80% training set and a 20% test set.

**Models Training and Evaluation**

Three models were trained:
- Logistic Regression (Multinomial)
- Random Forest Classifier
- Naive Bayes Classifier

Metrics used:
- Precision (correctly predicted positives over total predicted positives)
- Recall (correctly predicted positives over total actual positives)
- F1 Score (harmonic mean of precision and recall)

**Results**

### Classification Model Results

| Class | Model                | Precision | Recall | F1 Score |
|-------|----------------------|-----------|--------|----------|
| High  | Logistic Regression  | 1.00      | 1.00   | 1.00     |
|       | Random Forest        | 1.00      | 1.00   | 1.00     |
|       | Naive Bayes          | 0.99      | 0.53   | 0.38     |
| Mid   | Logistic Regression  | 1.00      | 0.99   | 0.99     |
|       | Random Forest        | 0.99      | 0.99   | 0.99     |
|       | Naive Bayes          | 0.00      | 0.00   | 0.00     |
| Low   | Logistic Regression  | 1.00      | 1.00   | 1.00     |
|       | Random Forest        | 1.00      | 1.00   | 1.00     |
|       | Naive Bayes          | 0.60      | 0.44   | 0.44     |


**Interpretation and Insights**

Logistic Regression (Multinomial):
- Achieved perfect or near-perfect classification for all classes.
- F1-scores for "high" and "low" were 1.00, and for "mid" it was 0.99.
- The confusion matrix showed very few misclassifications, suggesting excellent generalization.
- Logistic Regression handles this problem exceptionally well due to the balanced and structured feature space (e.g., log-transformed features, scaled inputs).
<img width="584" alt="Screenshot 2025-05-27 at 11 07 58" src="https://github.com/user-attachments/assets/333d7c4f-bc2a-4c9b-b4b3-8e4cfa873b9b" />

Random Forest Classifier:
- Also achieved excellent performance, nearly matching Logistic Regression.
- Perfect scores for "low" and "high", with "mid" class also predicted almost perfectly.
- Random Forest effectively captured non-linear relationships and feature interactions, making it a robust alternative to Logistic Regression.
<img width="582" alt="Screenshot 2025-05-27 at 11 09 13" src="https://github.com/user-attachments/assets/88f97ac0-035f-4623-8073-32037b42f515" />

Naive Bayes Classifier:
- Performance was substantially weaker compared to the other models.
- Mid-class completely missed (F1-score = 0.00).
- Struggled with imbalances and feature correlations inherent in the dataset.
- Naive Bayes' strong independence assumptions likely led to poor generalization, especially for overlapping classes like "mid".
<img width="598" alt="Screenshot 2025-05-27 at 11 10 19" src="https://github.com/user-attachments/assets/ff7efeba-fc7b-4427-81d1-f1aba167da70" />


- Both Logistic Regression and Random Forest displayed near-perfect matrices, with almost no off-diagonal errors, however, Naive Bayes misclassified a significant portion of "mid" and "low" classes, often confusing them for each other or defaulting to majority classes.
<img width="970" alt="Screenshot 2025-05-27 at 11 11 41" src="https://github.com/user-attachments/assets/1b46d452-7869-4bc5-9751-8bb0b2c27456" />

**Conclusion**

For predicting IMDb rating groups:
- Logistic Regression is the best-performing model, providing near-perfect accuracy and strong generalization.
- Random Forest is also a strong candidate, offering robustness and similar performance.
- Naive Bayes is not suitable for this problem, as it struggles with feature dependencies and overlapping class distributions.


**Recommendations for Further Work**
While the current models provide valuable insights, several areas can be improved to enhance prediction accuracy and model robustness:
- Feature Expansion: Add more pre-release features like marketing budget, release window, star power, and franchise status.
- Class Balancing: Apply techniques like SMOTE or class weighting to address any remaining imbalances.
- Error Analysis: Review misclassified samples and residuals to uncover model weaknesses.
- Real-World Testing: Validate models on upcoming films using only pre-release data.




## **References**

- [IMDb Datasets](https://www.imdb.com/interfaces/) – Used for movie ratings, votes, genres, and production years.
- [TMDb API](https://developer.themoviedb.org/docs) – Source for movie budgets and revenue data.
- [Rotten Tomatoes](https://www.rottentomatoes.com) – Used for critic ratings (Fresh/Rotten).
- [Box Office Mojo](https://www.boxofficemojo.com/) – Reference for box office revenue data.
- [Pandas Documentation](https://pandas.pydata.org/docs/) – For data manipulation and analysis.
- [NumPy Documentation](https://numpy.org/doc/) – For numerical operations and transformations.
- [scikit-learn Documentation](https://scikit-learn.org/stable/) – For machine learning models, preprocessing tools, and evaluation metrics.
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) – For visualizations.
- [Seaborn Documentation](https://seaborn.pydata.org/) – For advanced visualizations.
- [MultiLabelBinarizer (scikit-learn)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html) – For encoding multi-label genre data.
- [Random Forest Algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [Logistic Regression Algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [Gradient Boosting Algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)
- [Naive Bayes Algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)
- [ChatGPT (OpenAI, GPT-4)](https://openai.com/) – Assisted with model explanations, code structuring, and report writing.














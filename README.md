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

## **Expected Outcomes**
- Identification of the most influential factors in determining box office success.
- Predictive insights on how pre-release attributes affect revenue potential.
- Data-driven recommendations for movie studios to optimize investment decisions.

## **Project Timeline**

- **March 10:** Submit project proposal.
- **March 11-25:** Data collection and preliminary analysis.
- **March 26 - April 10:** Exploratory Data Analysis (EDA) and hypothesis testing.
- **April 11-25:** Machine learning modeling and visualization.
- **May 23:** Final insights and conclusions.
- **May 30:** Final submission and report presentation.

This project will provide valuable insights into the factors influencing box office success, offering a data-driven approach to understanding the film industry’s financial dynamics.


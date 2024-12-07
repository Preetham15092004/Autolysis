# Data Analysis Report

## Data Summary

### Dataset Overview

- **Shape**: The dataset contains **2,652 rows** and **8 columns** (features). 
- **Missing Values**: 
  - The `date` column has **99 missing values**.
  - The `by` column has a significant **262 missing values**.
  - No missing values were found in `language`, `type`, `title`, `overall`, `quality`, and `repeatability`.
  
- **Data Types**:
  - **Categorical (`object`)**: `date`, `language`, `type`, `title`, `by`
  - **Numerical (`int64`)**: `overall`, `quality`, `repeatability`

### Initial Data Observation (Head of the Dataset)

The first five records are as follows:

| Date       | Language | Type  | Title        | By                             | Overall | Quality | Repeatability |
|------------|----------|-------|--------------|--------------------------------|---------|---------|---------------|
| 15-Nov-24  | Tamil    | movie | Meiyazhagan  | Arvind Swamy, Karthi          | 4       | 5       | 1             |
| 10-Nov-24  | Tamil    | movie | Vettaiyan    | Rajnikanth, Fahad Fazil       | 2       | 2       | 1             |
| 09-Nov-24  | Tamil    | movie | Amaran       | Siva Karthikeyan, Sai Pallavi | 4       | 4       | 1             |
| 11-Oct-24  | Telugu   | movie | Kushi        | Vijay Devarakonda, Samantha    | 3       | 3       | 1             |
| 05-Oct-24  | Tamil    | movie | GOAT         | Vijay                          | 3       | 3       | 1             |

### Correlation Analysis

The correlation between the numerical variables reveals:

- **Overall vs. Quality**: Strong positive correlation (0.83)
- **Overall vs. Repeatability**: Moderate positive correlation (0.51)
- **Quality vs. Repeatability**: Weak to moderate correlation (0.31)

## Insights

1. **Missing Values Handling**: The missing values in the `date` and `by` columns need attention. Imputation methods or excluding these rows might be considered based on the analysis goals.

2. **Datetime Conversion**: The `date` column should be converted to a datetime format to facilitate time-based analysis.

3. **Categorical Insights**: The dataset includes a mix of languages, which may allow the identification of regional trends or preferences.

4. **Ratings Analysis**: The presence of varied ratings for `overall`, `quality`, and `repeatability` provides a rich ground for exploring trends and correlations.

5. **Further Exploration**: The correlations suggest potential areas for regression analysis, with the possibility of predicting ratings based on other features.

## Potential Considerations for Analysis

1. **Exploratory Data Analysis (EDA)**: Visualizations can expand the understanding of the data distributions and the connections among features.
2. **Statistical Modeling**: Consider using regression models to explore how quality and repeatability can predict overall ratings.
3. **Content Analysis**: Investigating the relationships between contributors (`by`) and ratings could yield insightful patterns on collaborative works.

## Visualizations

![Correlation Matrix](./correlation_matrix_resized.png)
![Overall Distribution](./overall_distribution_resized.png)
![Quality Distribution](./quality_distribution_resized.png)
![Repeatability Distribution](./repeatability_distribution_resized.png)
![Date Bar Chart](./date_bar_chart_resized.png)
![Language Bar Chart](./language_bar_chart_resized.png)
![Type Bar Chart](./type_bar_chart_resized.png)

## Conclusion

The dataset is rich with information and presents several opportunities for exploration and analysis. Addressing the missing values and appropriately leveraging the dataset’s features will be crucial to derive actionable insights. Further visualizations and analyses will enhance the understanding of trends and relationships within the data.
# Dataset Analysis Report

## Dataset Overview

- **Shape**: The dataset consists of **2,652 rows** and **8 columns**, suggesting a sizeable amount of data relative to the number of features.

## Missing Values

- **Missing Values Count**:
  - The `date` column has **99 missing values**, approximately **3.7%** of the data. This could potentially impact analyses related to trends over time.
  - The `by` column has **262 missing values**, about **9.9%** of the dataset, indicating a significant lack of information about contributors or creators. 
  - Other columns have **no missing values**.

## Data Types

- **Dtypes**:
  - Most columns are of `object` type, except for `overall`, `quality`, and `repeatability`, which are integers. This aligns with their expected content.
  - The `date` column is listed as an `object`, which may complicate date-related analyses. It should ideally be converted to a datetime format.

## Head of the Dataset

- **Preview of Data**:
  - The sample titles reveal that the dataset primarily deals with **movies**, with a focus on language and type.
  - It includes critical evaluation metrics: **overall**, **quality**, and **repeatability**, providing insights into each movie's ratings.

## Correlations

- **Correlations Insights**:
  - The correlation between `overall` and `quality` is quite high at **0.83**, suggesting that as the overall rating increases, the quality rating also tends to increase.
  - The correlation between `overall` and `repeatability` is moderate (**0.51**), indicating some relationship—higher overall rated movies are somewhat more likely to be rated highly for repeatability.
  - A weaker correlation between `quality` and `repeatability** (0.31) suggests that these features may reflect distinct aspects of the movies' appeal.

## Implications for Analysis

1. **Handling Missing Values**:
   - Consider data imputation strategies for missing `date` and `by` entries. Alternatively, assess the impact of removing these entries on the analysis.

2. **Data Type Conversion**:
   - Convert the `date` column to a proper datetime format to facilitate time series analysis or any operations that depend on date manipulations.

3. **Deeper Analysis of Correlations**:
   - The correlations suggest relationships among the ratings, warranting further statistical analysis (e.g., regression) to explore these relationships in more detail.
   - Compute descriptive statistics and explore visualizations (like scatter plots for quantitative correlations) for deeper insights.

4. **Exploring Language and Type**:
   - Examine how ratings differ across languages and movie types to yield valuable insights regarding audience preferences.

5. **Movie Popularity and Reviewer Impact**:
   - The significant missing data in the `by` column limits insights into the influence of reviewers on ratings, yet, it can be valuable when present.

---

## Visualizations

Below are charts reflecting various aspects of the dataset:

### Correlation Matrix
![Chart](./media/correlation_matrix_resized.png)

### Overall Distribution
![Chart](./media/overall_distribution_resized.png)

### Quality Distribution
![Chart](./media/quality_distribution_resized.png)

### Repeatability Distribution
![Chart](./media/repeatability_distribution_resized.png)

### Date Bar Chart
![Chart](./media/date_bar_chart_resized.png)

### Language Bar Chart
![Chart](./media/language_bar_chart_resized.png)

### Type Bar Chart
![Chart](./media/type_bar_chart_resized.png)

---

The dataset presents rich opportunities for analysis, particularly regarding relationships between different ratings and the categorical properties of the movies. Further exploration is recommended to capitalize on these insights.
# Data Analysis Report on Well-being and Socioeconomic Factors

## 1. Dataset Overview
- **Shape**: The dataset consists of **2363 rows** and **11 columns**, indicating data on 2363 observations (likely countries over time) and 11 attributes for analysis.

## 2. Attributes and Data Types
The dataset comprises the following columns:

| Column Name                             | Data Type |
|-----------------------------------------|-----------|
| Country name                            | string    |
| year                                    | integer   |
| Life Ladder                             | float     |
| Log GDP per capita                      | float     |
| Social support                          | float     |
| Healthy life expectancy at birth        | float     |
| Freedom to make life choices            | float     |
| Generosity                              | float     |
| Perceptions of corruption               | float     |
| Positive affect                         | float     |
| Negative affect                         | float     |

### Description of Attributes
- **Life Ladder**: A measure of subjective well-being.
- **Log GDP per capita**: Economic measure indicating the wealth of a country.
- **Social support**: Reflects the availability of community support.
- **Healthy life expectancy at birth**: Expected number of years a newborn can expect to live in good health.
- **Freedom to make life choices**: The extent of individual freedom experienced in society.
- **Generosity**: Measures of self-reported generosity.
- **Perceptions of corruption**: Indicates the public’s perception of corruption in society.
- **Positive affect**: Measure of positive emotions.
- **Negative affect**: Measure of negative emotions.

## 3. Missing Values
Missing values are present in several columns, notably:

| Attribute                           | Missing Values | Percentage Missing |
|-------------------------------------|----------------|--------------------|
| Generosity                          | 81             | 3.4%               |
| Perceptions of corruption           | 125            | 5.3%               |
| Log GDP per capita                 | 28             | 1.2%               |
| Social support                      | 13             | 0.6%               |
| Healthy life expectancy at birth    | 63             | 2.7%               |
| Freedom to make life choices        | 36             | 1.5%               |
| Positive affect                     | 24             | 1%                 |
| Negative affect                     | 16             | 0.7%               |

This missing data could impact the analysis and might need to be addressed through imputation or exclusion, depending on the analysis method.

## 4. Correlation Analysis
The correlation matrix provides insights into how different attributes relate to one another, with values ranging from -1 (perfect negative correlation) to 1 (perfect positive correlation).

### Strongest Correlations
- **Life Ladder** shows a strong positive correlation with:
  - **Log GDP per capita**: 0.78
  - **Social support**: 0.72
  - **Healthy life expectancy**: 0.71

These strong correlations suggest that countries with higher GDP per capita, better health, and social support tend to report higher well-being.

### Corruption Insights
- **Negative correlation** with well-being indicators such as:
  - **Life Ladder**: -0.43
  - **Positive affect**: -0.27
  - **Freedom to make life choices**: -0.47

This indicates that higher perceived corruption is linked to lower life satisfaction and happiness.

### Negative Affect
- Has a substantial correlation with:
  - **Negative correlation with Life Ladder**: -0.35, suggesting that as negative emotions increase, life satisfaction decreases.

## 5. Implications
The data could be used to infer how socioeconomic factors (like GDP and social support) and individual perceptions (like freedom and corruption) interplay to affect overall happiness and well-being. An emphasis on improving GDP per capita and social support systems may enhance life satisfaction, while addressing corruption perceptions could also contribute positively.

## 6. Next Steps for Analysis
1. **Handling Missing Values**: Determine appropriate strategies (e.g., imputation or removal) for the missing data.
2. **In-depth Analysis**: Utilize regression models to explore the impact of GDP, social support, etc., on the Life Ladder while controlling for confounding factors.
3. **Visualizations**: Create visual representations (scatter plots, box plots) of relationships and distributions for deeper insights.

## Conclusion
The dataset serves as a rich resource for studying the factors contributing to well-being across various nations and times, providing a foundation for both exploratory and predictive analyses.

---

## Included Visualizations
![Correlation Matrix](./correlation_matrix_resized.png)
![Year Distribution](./year_distribution_resized.png)
![Life Ladder Distribution](./Life_Ladder_distribution_resized.png)
![Log GDP per Capita Distribution](./Log_GDP_per_capita_distribution_resized.png)
![Country Name Bar Chart](./Country_name_bar_chart_resized.png)
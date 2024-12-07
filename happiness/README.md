# Dataset Report: Life Satisfaction and Happiness Indicators

## Data Summary
The dataset comprises 2363 entries and 11 columns, capturing various factors influencing life satisfaction across different countries over time.

### 1. **Dataset Structure**
- **Shape**: The dataset contains **2363 rows** (observations) and **11 columns** (variables).

### 2. **Missing Values**
There are several fields with missing values, which should be addressed in subsequent analyses:
- **Log GDP per capita**: 28 missing values
- **Social support**: 13 missing values
- **Healthy life expectancy at birth**: 63 missing values
- **Freedom to make life choices**: 36 missing values
- **Generosity**: 81 missing values
- **Perceptions of corruption**: 125 missing values
- **Positive affect**: 24 missing values
- **Negative affect**: 16 missing values
- No missing values are present for **Country name**, **year**, and **Life Ladder**.

### 3. **Data Types**
- **Country name**: `object` (categorical)
- **year**: `int64` (numerical)
- Remaining columns: `float64` (numerical), indicating they contain continuous variables.

### 4. **Sample of the Data**
Here are the first five records from the dataset, showing data for Afghanistan over the years 2008-2012:

| Country name | year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|--------------|------|-------------|---------------------|----------------|---------------------------------|------------------------------|------------|---------------------------|-----------------|-----------------|
| Afghanistan  | 2008 | 3.724       | 7.350               | 0.451          | 50.5                            | 0.718                        | 0.164      | 0.882                     | 0.414           | 0.258           |
| Afghanistan  | 2009 | 4.402       | 7.509               | 0.552          | 50.8                            | 0.679                        | 0.187      | 0.850                     | 0.481           | 0.237           |
| Afghanistan  | 2010 | 4.758       | 7.614               | 0.539          | 51.1                            | 0.600                        | 0.118      | 0.707                     | 0.517           | 0.275           |
| Afghanistan  | 2011 | 3.832       | 7.581               | 0.521          | 51.4                            | 0.496                        | 0.160      | 0.731                     | 0.480           | 0.267           |
| Afghanistan  | 2012 | 3.783       | 7.661               | 0.521          | 51.7                            | 0.531                        | 0.234      | 0.776                     | 0.614           | 0.268           |

### 5. **Correlations**
Correlation coefficients among different variables reveal interesting insights:
- **Life Ladder** demonstrates strong positive correlations with:
  - **Log GDP per capita** (0.784)
  - **Social support** (0.723)
  - **Healthy life expectancy at birth** (0.715)
  - **Freedom to make life choices** (0.538)
  - **Positive affect** (0.515)
- Notable negative correlations exist for **Life Ladder** with:
  - **Perceptions of corruption** (-0.430)
  - **Negative affect** (-0.352)

Additionally:
- **Log GDP per capita** shows a strong correlation with **Healthy life expectancy at birth** (0.819).
- Correlations with **Generosity** are generally low to moderate, indicating it may not be as impactful on life satisfaction compared to economic or social factors.

## Conclusion
The dataset is well-structured but requires addresses to missing values to ensure data completeness and integrity. Identified strong correlations, particularly between economic factors (like GDP) and quality of life measures (such as Social Support and Life Ladder), suggest critical relationships that warrant further investigation. Future analyses could include statistical testing or predictive modeling to provide deeper insights into these interrelationships.

## Visualizations
Here are some visualizations depicting various aspects of the data:

![Correlation Matrix](./happiness/correlation_matrix_resized.png)
![Year Distribution](./happiness/year_distribution_resized.png)
![Life Ladder Distribution](./happiness/Life_Ladder_distribution_resized.png)
![Log GDP per Capita Distribution](./happiness/Log_GDP_per_capita_distribution_resized.png)
![Country Name Bar Chart](./happiness/Country_name_bar_chart_resized.png)
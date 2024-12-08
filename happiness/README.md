# Dataset Report: Well-being and Economic Factors Across Countries

## Data Summary
This report summarizes a dataset that focuses on various metrics related to well-being, economic factors, and social attributes across different countries and years. Below are the specific characteristics of the dataset:

- **Shape**: (2363, 11)
- **Missing Values**:
  - `Country name`: 0
  - `year`: 0
  - `Life Ladder`: 0
  - `Log GDP per capita`: 28
  - `Social support`: 13
  - `Healthy life expectancy at birth`: 63
  - `Freedom to make life choices`: 36
  - `Generosity`: 81
  - `Perceptions of corruption`: 125
  - `Positive affect`: 24
  - `Negative affect`: 16
- **Data Types**:
  - `Country name`: object
  - `year`: int64
  - Remaining columns: float64
- **Sample Data (Head)**:
```plaintext
| Country name  | year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|---------------|------|-------------|---------------------|-----------------|-------------------------------|-----------------------------|-------------|--------------------------|-----------------|-------------------|
| Afghanistan   | 2008 | 3.724       | 7.35                | 0.451           | 50.5                          | 0.718                       | 0.164       | 0.882                    | 0.414           | 0.258             |
| Afghanistan   | 2009 | 4.402       | 7.509               | 0.552           | 50.8                          | 0.679                       | 0.187       | 0.85                     | 0.481           | 0.237             |
| Afghanistan   | 2010 | 4.758       | 7.614               | 0.539           | 51.1                          | 0.6                         | 0.118       | 0.707                    | 0.517           | 0.275             |
| Afghanistan   | 2011 | 3.832       | 7.581               | 0.521           | 51.4                          | 0.496                       | 0.16        | 0.731                    | 0.48            | 0.267             |
| Afghanistan   | 2012 | 3.783       | 7.661               | 0.521           | 51.7                          | 0.531                       | 0.234       | 0.776                    | 0.614           | 0.268             |
```

### Correlation Matrix
The correlation matrix provides insights into the relationships between different variables. Here are several key findings:

- `Life Ladder` is strongly correlated with `Log GDP per capita` (0.78), suggesting that higher GDP levels are associated with better life satisfaction measures.
- There is also a high correlation (0.72) between `Social support` and `Life Ladder`, indicating the positive impact of social support on subjective well-being.

### Insights
#### 1. Dataset Structure
The dataset contains information on various well-being indicators over multiple years for different countries. It compiles complex interdependencies of social, economic, and emotional factors.

#### 2. Missing Values
Certain critical indicators, including `Generosity` and `Perceptions of corruption`, have a significant number of missing values. Addressing these gaps will be essential for accurate analysis.

#### 3. Data Types
The diversity of data types indicates a mixture of categorical (e.g., country names), temporal (years), and numerical information pertinent to well-being metrics.

#### 4. Correlation Analysis
Key observations regarding variable relationships were made, particularly regarding the strong positive correlations of well-being indicators with economic metrics. 

#### 5. Potential Data Issues
The substantial presence of missing values could limit analysis, and the weak correlation of `Generosity` raises questions about its role in measuring overall well-being in this context.

### Conclusion
This dataset serves as a valuable resource for examining how economic, social, and emotional factors converge to influence perceived well-being across nations. Future investigations might include:
- Addressing the missing values.
- Exploring visualizations to depict trends and relationships.
- Applying predictive modeling techniques to estimate life satisfaction based on economic and social predictors.

## Visual Representations
Below are charts that illustrate various aspects of the dataset.

![Correlation Matrix](correlation_matrix_resized.png)
![Year Distribution](year_distribution_resized.png)
![Life Ladder Distribution](Life_Ladder_distribution_resized.png)
![Log GDP per Capita Distribution](Log_GDP_per_capita_distribution_resized.png)
![Country Name Bar Chart](Country_name_bar_chart_resized.png) 

These visualizations can help convey the distribution and relationships within the dataset more clearly. 

--- 

This report aims to facilitate further analysis and discussions regarding the relationships captured in the data and depict the importance of various metrics in assessing life satisfaction across global contexts.
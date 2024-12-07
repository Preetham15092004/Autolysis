# Data Report on Book Dataset

## Data Summary
The dataset summarized contains 10,000 entries, comprising information about books across 23 attributes (columns).

### 1. Structure
- **Shape**: The dataset contains **10,000 rows** and **23 columns**.

### 2. Missing Values
Several columns feature missing values:
- **isbn**: 700 missing values
- **isbn13**: 585 missing values
- **original_publication_year**: 21 missing values
- **original_title**: 585 missing values
- **language_code**: 1,084 missing values

Other columns have no missing values, indicating that they are complete. Addressing these missing values is crucial for comprehensive analysis.

### 3. Data Types
- **Numerical Types**: 
  - ID columns (e.g., `book_id`, `goodreads_book_id`, etc.) are of type `int64`.
  - Columns like `average_rating`, `original_publication_year`, and `isbn13` are represented as `float64`, whereas `ratings_count`, `work_ratings_count`, and others are `int64`.
  
- **Categorical/Non-numeric Types**: 
  - Columns such as `isbn`, `authors`, `original_title`, `title`, and `language_code` are stored as `object`. These necessitate specific encoding or processing for numerical analysis.

### 4. Sample Data (Head)
The first five entries provide as follows:
| book_id | goodreads_book_id | best_book_id | work_id  | books_count | isbn        | isbn13           | authors                                     | original_publication_year | original_title                                      | title                                                       | language_code | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 | image_url                                                                                 | small_image_url                                                                                |
|---------|-------------------|---------------|----------|-------------|-------------|------------------|---------------------------------------------|----------------------------|-----------------------------------------------------|------------------------------------------------------------|---------------|----------------|---------------|---------------------|--------------------------|-----------|-----------|-----------|-----------|-----------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| 1       | 2767052           | 2767052       | 2792775  | 272         | 439023483   | 9780439023480.0  | Suzanne Collins                            | 2008.0                     | The Hunger Games                                   | The Hunger Games (The Hunger Games, #1)                  | eng           | 4.34           | 4780653       | 4942365             | 155254                   | 66715     | 127936    | 560092    | 1481305   | 2706317   | https://images.gr-assets.com/books/1447303603m/2767052.jpg                              | https://images.gr-assets.com/books/1447303603s/2767052.jpg                                   |
| 2       | 3                 | 3             | 4640799  | 491         | 439554934   | 9780439554930.0  | J.K. Rowling, Mary GrandPré                | 1997.0                     | Harry Potter and the Philosopher's Stone          | Harry Potter and the Sorcerer's Stone (Harry Potter, #1) | eng           | 4.44           | 4602479       | 4800065             | 75867                    | 75504     | 101676    | 455024    | 1156318   | 3011543   | https://images.gr-assets.com/books/1474154022m/3.jpg                                      | https://images.gr-assets.com/books/1474154022s/3.jpg                                        |
| 3       | 41865             | 41865         | 3212258  | 226         | 316015849   | 9780316015840.0  | Stephenie Meyer                             | 2005.0                     | Twilight                                           | Twilight (Twilight, #1)                                   | en-US         | 3.57           | 3866839       | 3916824             | 95009                    | 456191    | 436802    | 793319    | 875073    | 1355439   | https://images.gr-assets.com/books/1361039443m/41865.jpg                                 | https://images.gr-assets.com/books/1361039443s/41865.jpg                                    |
| 4       | 2657              | 2657          | 3275794  | 487         | 61120081    | 9780061120080.0  | Harper Lee                                  | 1960.0                     | To Kill a Mockingbird                             | To Kill a Mockingbird                                      | eng           | 4.25           | 3198671       | 3340896             | 72586                    | 60427     | 117415    | 446835    | 1001952   | 1714267   | https://images.gr-assets.com/books/1361975680m/2657.jpg                                  | https://images.gr-assets.com/books/1361975680s/2657.jpg                                     |
| 5       | 4671              | 4671          | 245494   | 1356        | 743273567   | 9780743273560.0  | F. Scott Fitzgerald                          | 1925.0                     | The Great Gatsby                                   | The Great Gatsby                                            | eng           | 3.89           | 2683664       | 2773745             | 51992                    | 86236     | 197621    | 606158    | 936012    | 947718    | https://images.gr-assets.com/books/1490528560m/4671.jpg                                  | https://images.gr-assets.com/books/1490528560s/4671.jpg                                     |

### 5. Correlations
The correlation matrix indicates relationships between numeric variables:
- **`ratings_count`** and **`work_ratings_count`** exhibit a strong correlation (0.995), suggesting both metrics gauge similar popularity.
- **Negative correlations** between `books_count` and various rating metrics suggest a potential inverse relationship; as the number of books related to a title increases, individual book ratings may decrease.
- **Average ratings** positively correlate with `ratings_5` and negatively with lower ratings (`ratings_1` to `ratings_4`), which follows expected patterns.

## Insights and Next Steps
1. **Missing Data Handling**: Investigate handling methods for missing data in critical columns like `isbn` and `language_code`, possibly using imputation or data removal for minimal deficiencies.

2. **Data Cleaning**: Ensure `isbn` and `isbn13` are well-formatted and any inconsistencies are addressed.

3. **Exploratory Data Analysis (EDA)**: Conduct EDA to visualize the distribution of ratings, counts, and publication years, aiding in understanding trends in book popularity and reader preferences.

4. **Modeling and Prediction**: Consider machine learning models to predict book ratings based on features such as authors, publication year, and work counts. Correlational data could inform feature selection and model complexity.

5. **Content Analysis**: Further analysis on qualitative attributes (like `original_title`, `authors`, etc.) to uncover themes or genres that are particularly favored by readers.

---

### Visual Representations
![Correlation Matrix](./correlation_matrix_resized.png)

![Book ID Distribution](./book_id_distribution_resized.png)

![Goodreads Book ID Distribution](./goodreads_book_id_distribution_resized.png)

![Best Book ID Distribution](./best_book_id_distribution_resized.png)

![ISBN Bar Chart](./isbn_bar_chart_resized.png)

![Authors Bar Chart](./authors_bar_chart_resized.png)

![Original Title Bar Chart](./original_title_bar_chart_resized.png)

In summary, this dataset presents a compelling opportunity for analysis concerning book popularity and reader preferences; however, preliminary steps involving cleaning and handling missing values are essential before further exploration can occur.
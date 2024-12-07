# Book Dataset Analysis

## Data Summary
This report provides a comprehensive summary of a dataset containing details about 10,000 books, likely sourced from a platform like Goodreads. The dataset includes various attributes for each book, contributing to a robust analysis of book popularity, ratings, and characteristics.

### Structure
- **Shape:** The dataset contains **10,000 rows** and **23 columns**, indicating a substantial collection.

### Missing Values
The analysis reveals several columns with missing values:
- **Total Missing Values:** 
  - `isbn`: 700
  - `isbn13`: 585
  - `original_publication_year`: 21
  - `original_title`: 585
  - `language_code`: 1084

This indicates potential data quality issues, particularly in identifiers and language specifications.

### Data Types
The dataset comprises a variety of data types:
- **Integer (`int64`)**: Various identifiers and count variables such as `book_id`, `work_id`, and `ratings_count`.
- **Floating Point (`float64`)**: Numerical values including `isbn13` and `average_rating`.
- **String (`object`)**: Textual fields such as book titles, authors, ISBNs, and image URLs.

### Sample Data
The first five records (head) showcase:
- Titles like "The Hunger Games" and "To Kill a Mockingbird."
- A notable average rating, with several books rated above 4.0.

### Correlations
The correlation matrix provides insights into relationships between different attributes:
- **Strong Positive Correlations**: Notably, there’s a very strong correlation between `ratings_count` and `work_ratings_count` (0.995). 
- **Significant Relationships**: Other rating categories (`ratings_1` through `ratings_5`) exhibit strong correlations with one another, suggesting trends in user ratings.
- **Negative Correlations**: For instance, `books_count` negatively correlates with `average_rating`, indicating that books with higher ratings may not always be the most numerous in terms of reviews.

### Additional Insights
1. **High Missing Values in ISBNs**: The high number of missing values in `isbn` and `isbn13` can challenge data integrity, as these are essential for book identification.
2. **Diversity in Publication Years**: A diverse range of publication years indicates various genres and audiences, as older works are present alongside contemporary literature.
3. **Image URLs for User Engagement**: The inclusion of image URLs demonstrates a user-friendly database emphasizing visual representation.
4. **Potential for Further Analysis**:
   - Trends in publishing over time via `original_publication_year`.
   - Popularity analysis using `ratings_count` compared to `average_rating`.
   - Analyzing author popularity through the `authors` column, with insights into correlations with ratings and reviews.

### Conclusion
The dataset serves as a rich resource for analyzing books, their attributes, and ratings. Addressing the missing values is crucial for ensuring data quality. The strong correlations identified within the dataset point to significant relationships worth exploring in future analyses.

## Visualizations
The following charts provide further insights into the data:

![Correlation Matrix](./goodreads/correlation_matrix_resized.png)
![Book ID Distribution](./goodreads/book_id_distribution_resized.png)
![Goodreads Book ID Distribution](./goodreads/goodreads_book_id_distribution_resized.png)
![Best Book ID Distribution](./goodreads/best_book_id_distribution_resized.png)
![ISBN Bar Chart](./goodreads/isbn_bar_chart_resized.png)
![Authors Bar Chart](./goodreads/authors_bar_chart_resized.png)
![Original Titles Bar Chart](./goodreads/original_title_bar_chart_resized.png)
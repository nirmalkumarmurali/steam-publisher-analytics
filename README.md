# Steam Games Publisher & Developer Analytics

## What This Project Does

Analyses 10,000+ Steam games to identify which publishers and developers have the most successful portfolios, using estimated ownership data, review sentiment, playtime, and concurrent users.

This project covers two layers of analysis:
- **Python (Pandas)** — data cleaning, transformation, and aggregation
- **SQL (SQLite)** — querying and exploring the same dataset using structured queries

## Key Questions Answered

1. Which publishers have the most estimated game owners overall?
2. Which publishers make the most consistently loved games?
3. Which developers generate the most total reviews?
4. Which free games are both massively played AND highly rated?
5. What does the price distribution look like across publisher catalogs?

## Key Findings

- Biggest publisher by estimated owners: **Valve** (150M+ for CS:GO alone)
- Most consistently loved publisher (3+ games, high CCU): **Red Barrels** (93.7% avg rating)
- Most loved single game: **Portal 2** (98.7% positive reviews)
- Valve does NOT appear in the top 10 most loved publishers — smaller studios consistently outperform them on quality
- Free games with CCU > 10,000 AND rating > 80% represent a small but elite group of titles

## Project Structure

```
steam-publisher-analytics/
├── steam_analysis.ipynb      ← Python analysis notebook (Pandas)
├── steam_queries.sql         ← SQL queries for the same dataset
├── steam_games_dataset.csv   ← Raw dataset (10,000+ games)
├── README.md
├── LICENSE
└── .gitignore
```

## Skills Demonstrated

### Python (Pandas)
- Loading and exploring real-world CSV data
- Handling missing values with `isnull().sum()`
- Cleaning messy string data — parsing `"1,000,000 .. 2,000,000"` into numeric midpoints
- Creating calculated columns (positive ratio, price in EUR, playtime in hours)
- Filtering data for statistical reliability (min 100 reviews)
- Aggregating with `groupby().agg()` across multiple metrics
- Sorting and ranking publisher/developer portfolios

### SQL (SQLite)
- `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`
- `GROUP BY` with `COUNT()`, `AVG()`, `SUM()`, `MAX()`
- `HAVING` to filter aggregated groups
- Calculated fields inside queries
- Multi-condition filtering combining `WHERE` and `HAVING`

### Other
- Git version control and GitHub project management
- Writing clean, commented, reproducible code
- Extracting business insights from raw data

## Dataset

- **Source:** [Kaggle — Steam Games Dataset](https://www.kaggle.com/datasets)
- **License:** CC0 Public Domain
- **Size:** ~10,000 games, 17 columns

## How to Run

### Python Analysis
```bash
pip install pandas numpy jupyter
jupyter notebook
```
Open `steam_analysis.ipynb` and run all cells from top to bottom.
The notebook will automatically export `publisher_stats.csv` and `steam_cleaned.csv`.

### SQL Analysis
1. Go to [sqliteonline.com](https://sqliteonline.com)
2. Import `steam_games_dataset.csv` (tick "First row is header")
3. Open `steam_queries.sql` and run any query

## Key Takeaways

- Messy real-world data requires thoughtful preparation — the `owners` column was stored as a string range (`"1,000,000 .. 2,000,000"`) and needed a custom parsing function to extract usable numeric values
- Statistical reliability matters in analysis — filtering out games with fewer than 100 reviews prevents misleading percentage calculations and ensures conclusions are based on meaningful sample sizes
- `GROUP BY` in SQL and `groupby().agg()` in Pandas are two different syntaxes solving the same analytical problem — knowing both gives flexibility across different data environments
- Scale does not equal quality — smaller studios like Red Barrels and Fireproof Games consistently outperform industry giants like Valve on quality metrics when portfolios are compared by average review sentiment
# Steam Games Publisher & Developer Analytics

**Solo Project — Week 1 | Nirmal Kumar Murali**

## What This Project Does
Analyses 10,000+ Steam games to identify which publishers and developers have the most successful portfolios, using estimated ownership data, review sentiment, playtime, and concurrent users.

## Key Questions Answered
1. Which publishers have the most estimated game owners overall?
2. Which developers consistently get the highest positive review ratios?
3. How does price relate to review scores?
4. Which games have the highest peak concurrent users (CCU)?

## Skills Demonstrated
- **Pandas**: loading, cleaning, groupby aggregations, calculated columns
- **Data Cleaning**: parsing messy string ranges into usable numbers (`owners` column)
- **Exploratory Data Analysis**: filtering, sorting, descriptive statistics
- **Python**: writing reusable functions, handling missing values

## Dataset
- Source: [Kaggle — Steam Games Dataset](https://www.kaggle.com/datasets)
- License: CC0 Public Domain
- Size: ~10,000 games, 17 columns

## How to Run
```bash
pip install pandas numpy
python steam_analysis.py
```

## Key Findings
- The `owners` column required custom parsing (string "1,000,000 .. 2,000,000" → numeric midpoint 1,500,000)
- 40% of games have fewer than 100 reviews — filtered out for meaningful analysis
- Top publishers by estimated ownership are dominated by a small number of large studios
- Several indie developers maintain 90%+ positive review ratios across 3+ games

## Files
| File | Description |
|------|-------------|
| `steam_analysis.py` | Main analysis script |
| `steam_cleaned.csv` | Cleaned dataset (output) |
| `publisher_stats.csv` | Aggregated publisher metrics (input for Power BI) |
| `developer_stats.csv` | Aggregated developer metrics (input for Power BI) |

## Next Step (Week 5)
Load `publisher_stats.csv` into Power BI to build an interactive dashboard with:
- Top 15 publishers by owners (bar chart)
- Review ratio vs game count (scatter plot)
- Price vs playtime correlation
- Publisher comparison slicers

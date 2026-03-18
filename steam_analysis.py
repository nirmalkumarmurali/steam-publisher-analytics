# Steam Games Publisher Analytics
# Week 1 Solo Project — Nirmal Kumar Murali
# Dataset: steam_games_dataset.csv (Kaggle, CC0 Public Domain)

import pandas as pd
import numpy as np

# ── 1. LOAD DATA ──────────────────────────────────────────────
df = pd.read_csv('steam_games_dataset.csv')

print("=== STEP 1: First look at the data ===")
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(df.head(3))
print(df.dtypes)
print()

# ── 2. UNDERSTAND MISSING VALUES ──────────────────────────────
print("=== STEP 2: Missing values per column ===")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
print(pd.DataFrame({'Missing Count': missing, 'Missing %': missing_pct}))
print()

# ── 3. CLEAN THE OWNERS COLUMN ────────────────────────────────
# owners looks like "1,000,000 .. 2,000,000" — we need a number
# We take the average of the two numbers in the range

print("=== STEP 3: Cleaning the 'owners' column ===")
print("Before cleaning (sample):", df['owners'].head(5).values)

def parse_owners(owners_str):
    """
    Converts "1,000,000 .. 2,000,000" into average: 1500000.0
    Returns NaN if string is missing or malformed.
    """
    if pd.isnull(owners_str):
        return np.nan
    try:
        # Remove commas, split on '..'
        parts = owners_str.replace(',', '').split('..')
        low = float(parts[0].strip())
        high = float(parts[1].strip())
        return (low + high) / 2  # take the midpoint
    except:
        return np.nan

df['owners_mid'] = df['owners'].apply(parse_owners)

print(f"After cleaning (sample):")
print(df[['owners', 'owners_mid']].head(5))
print(f"NaN count after cleaning: {df['owners_mid'].isnull().sum()}")
print()

# ── 4. ADD USEFUL CALCULATED COLUMNS ──────────────────────────
print("=== STEP 4: Adding calculated columns ===")

# Review ratio: what % of reviews are positive?
df['total_reviews'] = df['positive'] + df['negative']
df['positive_ratio'] = (df['positive'] / df['total_reviews'] * 100).round(1)

# Convert price from cents to euros
df['price_eur'] = (df['price'] / 100).round(2)

# Convert average playtime from minutes to hours
df['avg_playtime_hrs'] = (df['average_forever'] / 60).round(1)

print("New columns added: total_reviews, positive_ratio, price_eur, avg_playtime_hrs")
print(df[['name', 'price_eur', 'positive_ratio', 'avg_playtime_hrs']].head(5))
print()

# ── 5. FILTER FOR MEANINGFUL DATA ─────────────────────────────
print("=== STEP 5: Filtering for games with enough data ===")

# Only keep games with at least 100 reviews (otherwise % is meaningless)
df_filtered = df[df['total_reviews'] >= 100].copy()
print(f"Games with 100+ reviews: {len(df_filtered)} out of {len(df)}")
print()

# ── 6. PUBLISHER ANALYSIS ─────────────────────────────────────
print("=== STEP 6: Publisher Analytics ===")

publisher_stats = df_filtered.groupby('publisher').agg(
    game_count=('name', 'count'),
    total_owners=('owners_mid', 'sum'),
    avg_positive_ratio=('positive_ratio', 'mean'),
    total_reviews=('total_reviews', 'sum'),
    avg_price_eur=('price_eur', 'mean'),
    peak_ccu=('ccu', 'max')
).reset_index()

# Round for readability
publisher_stats['avg_positive_ratio'] = publisher_stats['avg_positive_ratio'].round(1)
publisher_stats['avg_price_eur'] = publisher_stats['avg_price_eur'].round(2)
publisher_stats['total_owners_M'] = (publisher_stats['total_owners'] / 1_000_000).round(2)

# Sort by total estimated owners
publisher_stats = publisher_stats.sort_values('total_owners', ascending=False)

print("Top 15 Publishers by Estimated Owners:")
top15 = publisher_stats.head(15)[['publisher','game_count','total_owners_M','avg_positive_ratio','peak_ccu']]
print(top15.to_string(index=False))
print()

# ── 7. DEVELOPER ANALYSIS ─────────────────────────────────────
print("=== STEP 7: Developer Analytics ===")

dev_stats = df_filtered.groupby('developer').agg(
    game_count=('name', 'count'),
    avg_positive_ratio=('positive_ratio', 'mean'),
    total_owners=('owners_mid', 'sum'),
    best_game=('name', lambda x: df_filtered.loc[x.index, 'owners_mid'].idxmax())
).reset_index()

dev_stats['avg_positive_ratio'] = dev_stats['avg_positive_ratio'].round(1)
dev_stats['total_owners_M'] = (dev_stats['total_owners'] / 1_000_000).round(2)

# Most loved developers (min 3 games, high positive ratio)
print("Most Loved Developers (3+ games, sorted by review score):")
loved = dev_stats[dev_stats['game_count'] >= 3].sort_values('avg_positive_ratio', ascending=False)
print(loved[['developer','game_count','avg_positive_ratio','total_owners_M']].head(10).to_string(index=False))
print()

# ── 8. KEY INSIGHTS ───────────────────────────────────────────
print("=== STEP 8: Key Insights (what you'd present in an interview) ===")

total_games = len(df)
total_with_reviews = len(df_filtered)
top_pub = publisher_stats.iloc[0]
top_dev_loved = loved.iloc[0]

print(f"1. Dataset contains {total_games:,} games; {total_with_reviews:,} have 100+ reviews")
print(f"2. Top publisher by estimated owners: {top_pub['publisher']} ({top_pub['total_owners_M']}M owners)")
print(f"3. Most loved developer (3+ games): {top_dev_loved['developer']} ({top_dev_loved['avg_positive_ratio']}% positive reviews)")
print(f"4. Average positive review ratio across all games: {df_filtered['positive_ratio'].mean():.1f}%")
print(f"5. Most expensive avg catalog: use publisher_stats sorted by avg_price_eur")

# ── 9. EXPORT CLEAN DATA ──────────────────────────────────────
df_filtered.to_csv('steam_cleaned.csv', index=False)
publisher_stats.to_csv('publisher_stats.csv', index=False)
dev_stats.to_csv('developer_stats.csv', index=False)
print()
print("=== Done! Files exported: steam_cleaned.csv, publisher_stats.csv, developer_stats.csv ===")
print("Next step: load publisher_stats.csv into Power BI!")

-- Steam Games Dataset - SQL Analysis
-- Author: Nirmal Kumar Murali
-- Dataset: steam_games_dataset.csv

-- ── 1. BASIC EXPLORATION ──────────────────────────────────────

-- View first 10 games
SELECT * FROM steam_games_dataset LIMIT 10;

SELECT name, developer, publisher, positive, negative
FROM steam_games_dataset
LIMIT 10;

-- ── 2. FILTERING ──────────────────────────────────────────────

-- only free games
SELECT name, publisher, price
FROM steam_games_dataset
WHERE price = 0
LIMIT 20;

-- ── 3. SORTING ────────────────────────────────────────────────

--Most positive reviews first 
SELECT name, publisher, price
FROM steam_games_dataset
ORDER BY positive DESC
LIMIT 10;
--Cheapest paid games
SELECT name, publisher, price
FROM steam_games_dataset
WHERE price > 0
ORDER BY price ASC
LIMIT 10;

-- ── 4. GROUPING & AGGREGATION ─────────────────────────────────

--How many games does each publisher have?
SELECT publisher, COUNT(*) AS game_count
FROM steam_games_dataset
GROUP BY publisher
ORDER BY game_count DESC
LIMIT 10;
-- Average positive reviews per publisher (min 5 games)
SELECT publisher,
	COUNT(*) AS game_count,
    AVG(positive) AS avg_positive
FROM steam_games_dataset
GROUP BY publisher
HAVING COUNT(*) >= 5
ORDER BY avg_positive DESC
LIMIT 10;
-- Total reviews per developer
SELECT developer,
       COUNT(*) AS game_count,
       SUM(positive + negative) AS total_reviews
FROM steam_games_dataset
GROUP BY developer
ORDER BY total_reviews DESC
LIMIT 10;

-- ── 5. ADVANCED QUERIES ───────────────────────────────────────

-- Find publishers with high quality games and avg ccu >1000 and minimum 3 games. 
SELECT publisher,
	COUNT(*) AS game_count,
    AVG(ccu) AS avg_ccu,
    AVG(positive * 100.0 / (positive + negative)) AS avg_rating
FROM steam_games_dataset
WHERE positive + negative > 100
GROUP BY publisher
HAVING COUNT(*) >= 3 AND AVG(ccu) > 1000
ORDER BY avg_rating DESC
LIMIT 10;
-- Price analysis by publisher (most expensive)
Select publisher,
	COUNT(*) AS game_count,
    AVG(price) / 100.0 AS avg_price_eur,
    MAX(price) / 100.0 AS most_expensive
FROM steam_games_dataset
WHERE price > 0
GROUP BY publisher
HAVING COUNT(*) >= 5
ORDER BY avg_price_eur DESC
LIMIT 10;
-- free popular quality games
SELECT name,
       developer,
       ccu,
       positive * 100 / (positive + negative) AS rating
FROM steam_games_dataset
WHERE price = 0
  AND ccu > 10000
  AND positive * 100 / (positive + negative) > 80
ORDER BY ccu DESC;SELECT * FROM steam_games_dataset LIMIT 10;

SELECT name, developer, publisher, positive, negative
FROM steam_games_dataset
LIMIT 10;
-- only free games
SELECT name, publisher, price
FROM steam_games_dataset
WHERE price = 0
LIMIT 20;
--Most positive reviews first 
SELECT name, publisher, price
FROM steam_games_dataset
ORDER BY positive DESC
LIMIT 10;
--Cheapest paid games
SELECT name, publisher, price
FROM steam_games_dataset
WHERE price > 0
ORDER BY price ASC
LIMIT 10;
--How many games does each publisher have?
SELECT publisher, COUNT(*) AS game_count
FROM steam_games_dataset
GROUP BY publisher
ORDER BY game_count DESC
LIMIT 10;
-- Average positive reviews per publisher (min 5 games)
SELECT publisher,
	COUNT(*) AS game_count,
    AVG(positive) AS avg_positive
FROM steam_games_dataset
GROUP BY publisher
HAVING COUNT(*) >= 5
ORDER BY avg_positive DESC
LIMIT 10;
-- Total reviews per developer
SELECT developer,
       COUNT(*) AS game_count,
       SUM(positive + negative) AS total_reviews
FROM steam_games_dataset
GROUP BY developer
ORDER BY total_reviews DESC
LIMIT 10;
-- Find publishers with high quality games and avg ccu >1000 and minimum 3 games. 
SELECT publisher,
	COUNT(*) AS game_count,
    AVG(ccu) AS avg_ccu,
    AVG(positive * 100.0 / (positive + negative)) AS avg_rating
FROM steam_games_dataset
WHERE positive + negative > 100
GROUP BY publisher
HAVING COUNT(*) >= 3 AND AVG(ccu) > 1000
ORDER BY avg_rating DESC
LIMIT 10;
-- Price analysis by publisher (most expensive)
Select publisher,
	COUNT(*) AS game_count,
    AVG(price) / 100.0 AS avg_price_eur,
    MAX(price) / 100.0 AS most_expensive
FROM steam_games_dataset
WHERE price > 0
GROUP BY publisher
HAVING COUNT(*) >= 5
ORDER BY avg_price_eur DESC
LIMIT 10;
-- free popular quality games
SELECT name,
       developer,
       ccu,
       positive * 100 / (positive + negative) AS rating
FROM steam_games_dataset
WHERE price = 0
  AND ccu > 10000
  AND positive * 100 / (positive + negative) > 80
ORDER BY ccu DESC;
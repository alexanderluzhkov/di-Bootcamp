-- Task 1:Update the heights of competitors
UPDATE olympics.person p
SET height = (
    SELECT ROUND(AVG(p2.height))
    FROM olympics.person p2
    JOIN olympics.person_region pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id = (
        SELECT pr.region_id
        FROM olympics.person_region pr
        WHERE pr.person_id = p.id
    )
    AND p2.height IS NOT NULL
)
WHERE p.height IS NULL;
-- Task 2: Create temporary table for multi-event competitors
CREATE TEMPORARY TABLE multi_event_competitors AS
WITH competitor_event_count AS (
    SELECT gc.person_id, gc.games_id, COUNT(DISTINCT ce.event_id) AS event_count
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    GROUP BY gc.person_id, gc.games_id
    HAVING COUNT(DISTINCT ce.event_id) > 1
)
SELECT p.id AS person_id, p.full_name, g.games_name, cec.event_count
FROM competitor_event_count cec
JOIN olympics.person p ON cec.person_id = p.id
JOIN olympics.games g ON cec.games_id = g.id;

-- Task 3: Identify regions with above-average medal counts
WITH competitor_medals AS (
    SELECT gc.person_id, pr.region_id, COUNT(ce.medal_id) AS medal_count
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN olympics.person_region pr ON gc.person_id = pr.person_id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY gc.person_id, pr.region_id
),
region_averages AS (
    SELECT region_id, AVG(medal_count) AS avg_medals_per_competitor
    FROM competitor_medals
    GROUP BY region_id
),
overall_average AS (
    SELECT AVG(medal_count) AS overall_avg_medals
    FROM competitor_medals
)
SELECT nr.region_name, ra.avg_medals_per_competitor
INTO TEMPORARY TABLE above_average_regions
FROM region_averages ra
JOIN olympics.noc_region nr ON ra.region_id = nr.id
CROSS JOIN overall_average oa
WHERE ra.avg_medals_per_competitor > oa.overall_avg_medals
ORDER BY ra.avg_medals_per_competitor DESC;

-- Task 4: Create temporary table for season participation
CREATE TEMPORARY TABLE season_participation AS
WITH competitor_seasons AS (
    SELECT DISTINCT gc.person_id, g.season
    FROM olympics.games_competitor gc
    JOIN olympics.games g ON gc.games_id = g.id
)
SELECT p.id AS person_id, p.full_name,
       MAX(CASE WHEN cs.season = 'Summer' THEN 1 ELSE 0 END) AS participated_summer,
       MAX(CASE WHEN cs.season = 'Winter' THEN 1 ELSE 0 END) AS participated_winter
FROM olympics.person p
JOIN competitor_seasons cs ON p.id = cs.person_id
GROUP BY p.id, p.full_name;

-- Display results
SELECT 'Multi-event competitors' AS result_type, COUNT(*) AS count FROM multi_event_competitors
UNION ALL
SELECT 'Above average medal regions' AS result_type, COUNT(*) AS count FROM above_average_regions
UNION ALL
SELECT 'Competitors in both seasons' AS result_type, COUNT(*) AS count 
FROM season_participation 
WHERE participated_summer = 1 AND participated_winter = 1;

-- Optionally, you can add more SELECT statements here to view the actual data in each temporary table
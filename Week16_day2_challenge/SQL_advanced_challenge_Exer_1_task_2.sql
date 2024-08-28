DROP TABLE IF EXISTS competitors_summer_winter_medals;

-- Create the temporary table
CREATE TEMPORARY TABLE competitors_summer_winter_medals AS
SELECT 
    gc.person_id,
    p.full_name,
    SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM 
    olympics.games_competitor gc
JOIN 
    olympics.games g ON gc.games_id = g.id
JOIN 
    olympics.competitor_event ce ON gc.id = ce.competitor_id
JOIN 
    olympics.person p ON gc.person_id = p.id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    gc.person_id, p.full_name
HAVING 
    SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) > 0 
    AND SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) > 0;

-- Display the contents of the temporary table
SELECT * FROM competitors_summer_winter_medals;

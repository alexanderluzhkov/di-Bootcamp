-- Drop the temporary table if it already exists
DROP TABLE IF EXISTS region_medal_count;

-- Create a temporary table to store the regions and their medal counts
CREATE TEMPORARY TABLE region_medal_count AS
SELECT 
    pr.region_id,
    nr.region_name,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.competitor_event ce
JOIN 
    olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN 
    olympics.person_region pr ON gc.person_id = pr.person_id
JOIN 
    olympics.noc_region nr ON pr.region_id = nr.id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    pr.region_id, nr.region_name;

-- Retrieve the regions with competitors who have won the highest number of medals in a single event
SELECT 
    nr.region_name,
    SUM(rmc.total_medals) AS total_medals
FROM 
    olympics.noc_region nr
JOIN 
    region_medal_count rmc ON nr.id = rmc.region_id
GROUP BY 
    nr.region_name
ORDER BY 
    total_medals DESC
LIMIT 5;

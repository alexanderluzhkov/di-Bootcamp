-- Create the temporary table with competitor names and their total medals
CREATE TEMPORARY TABLE competitor_medal_count AS
SELECT 
    gc.person_id,
    p.full_name,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.games_competitor gc
JOIN 
    olympics.competitor_event ce ON gc.id = ce.competitor_id
JOIN 
    olympics.person p ON gc.person_id = p.id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    gc.person_id, p.full_name;

-- Select competitors who have won more than 2 medals, ordered by total_medals in descending order
SELECT 
    person_id,
    full_name,
    total_medals
FROM 
    competitor_medal_count
WHERE 
    total_medals > 2
ORDER BY 
    total_medals DESC;

WITH medalist_ages AS (
  SELECT 
    gc.person_id,
    ce.medal_id,
    MIN(gc.age) AS age
  FROM 
    olympics.games_competitor gc
  JOIN 
    olympics.competitor_event ce ON gc.id = ce.competitor_id
  WHERE 
    ce.medal_id IS NOT NULL
  GROUP BY 
    gc.person_id, ce.medal_id
)
SELECT 
    m.medal_name, 
    AVG(ma.age) AS average_age
FROM 
    medalist_ages ma
JOIN 
    olympics.medal m ON ma.medal_id = m.id
GROUP BY 
    m.medal_name;

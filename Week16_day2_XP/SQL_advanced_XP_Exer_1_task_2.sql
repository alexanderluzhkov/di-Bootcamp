WITH competitor_event_counts AS (
  SELECT pr.region_id, gc.person_id,
         COUNT(DISTINCT ce.event_id) AS event_count
  FROM olympics.person_region pr
  JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
  JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
  GROUP BY pr.region_id, gc.person_id
  HAVING COUNT(DISTINCT ce.event_id) > 3
)
SELECT nr.region_name, COUNT(DISTINCT cec.person_id) AS competitor_count
FROM competitor_event_counts cec
JOIN olympics.noc_region nr ON cec.region_id = nr.id
GROUP BY nr.region_name
ORDER BY competitor_count DESC
LIMIT 5;
DELETE FROM competitor_medals
WHERE id IN (
  SELECT cm.id
  FROM competitor_medals cm
  LEFT JOIN olympics.games_competitor gc ON cm.id = gc.person_id
  LEFT JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
  GROUP BY cm.id
  HAVING SUM(CASE WHEN ce.medal_id IS NOT NULL THEN 1 ELSE 0 END) = 0
);

SELECT * FROM competitor_medals;
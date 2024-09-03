--Exersise 1
WITH BudgetGrowth AS (
    SELECT 
        pc.company_name,
        m.title,
        m.budget,
        m.release_date,
        LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) AS prev_budget,
        (m.budget - LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date)) / 
            NULLIF(LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date), 0) AS growth_rate
    FROM 
        movies.movie m
    JOIN 
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN 
        movies.production_company pc ON mc.company_id = pc.company_id
)
SELECT 
    company_name,
    AVG(growth_rate) AS avg_growth_rate
FROM 
    BudgetGrowth
WHERE 
    growth_rate IS NOT NULL
GROUP BY 
    company_name
ORDER BY 
    avg_growth_rate DESC;
--Exercise 2
WITH AverageRating AS (
    SELECT AVG(vote_average) AS overall_avg_rating
    FROM movies.movie
),
ActorRatings AS (
    SELECT 
        p.person_id,
        p.person_name,
        COUNT(m.movie_id) AS total_movies,
        COUNT(CASE WHEN m.vote_average > ar.overall_avg_rating THEN 1 END) AS above_avg_movies,
        RANK() OVER (ORDER BY COUNT(CASE WHEN m.vote_average > ar.overall_avg_rating THEN 1 END) DESC) AS rank
    FROM 
        movies.person p
    JOIN 
        movies.movie_cast mc ON p.person_id = mc.person_id
    JOIN 
        movies.movie m ON mc.movie_id = m.movie_id
    CROSS JOIN 
        AverageRating ar
    GROUP BY 
        p.person_id, p.person_name, ar.overall_avg_rating
)
SELECT 
    person_name,
    total_movies,
    above_avg_movies
FROM 
    ActorRatings
WHERE 
    rank = 1;
-- Task 3
WITH RankedMovies AS (
    SELECT 
        g.genre_name,
        m.title,
        m.release_date,
        m.revenue,
        ROW_NUMBER() OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS rn
    FROM 
        movies.movie m
    JOIN 
        movies.movie_genres mg ON m.movie_id = mg.movie_id
    JOIN 
        movies.genre g ON mg.genre_id = g.genre_id
)
SELECT 
    genre_name,
    title,
    release_date,
    revenue,
    AVG(revenue) OVER (
        PARTITION BY genre_name
        ORDER BY release_date DESC
        ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING
    ) AS rolling_avg_revenue
FROM 
    RankedMovies
WHERE 
    rn <= 3
ORDER BY 
    genre_name, release_date DESC;
-- Task 4
WITH MovieSeries AS (
    SELECT 
        k.keyword_name,  
        COUNT(DISTINCT m.movie_id) AS movie_count,
        SUM(m.revenue) AS total_revenue,
        RANK() OVER (ORDER BY SUM(m.revenue) DESC) AS revenue_rank
    FROM 
        movies.movie m
    JOIN 
        movies.movie_keywords mk ON m.movie_id = mk.movie_id
    JOIN 
        movies.keyword k ON mk.keyword_id = k.keyword_id
    GROUP BY 
        k.keyword_name  
    HAVING 
        COUNT(DISTINCT m.movie_id) > 1
)
SELECT 
    keyword_name AS series_keyword,  
    movie_count,
    total_revenue
FROM 
    MovieSeries
WHERE 
    revenue_rank = 1;


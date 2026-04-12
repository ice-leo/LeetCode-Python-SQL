-- Write your PostgreSQL query statement below

WITH agg AS (
    SELECT
        email,
        COUNT(email) AS count
    FROM
        Person
    GROUP BY email
)
SELECT
    email
FROM agg
WHERE count >= 2;

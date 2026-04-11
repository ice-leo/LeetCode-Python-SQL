```sql
-- Write your PostgreSQL query statement below
WITH ranked AS (
        SELECT
        salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS rank
    FROM Employee
    GROUP BY salary
)
SELECT
    MAX(salary) AS SecondHighestSalary -- max of nothing returns null
FROM ranked
WHERE rank = 2



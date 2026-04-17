-- Write your PostgreSQL query statement below


WITH merged AS (SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary,
    DENSE_RANK() OVER (PARTITION BY d.name ORDER BY salary DESC) AS rank
FROM Employee as e
LEFT JOIN Department as d
ON e.departmentID = d.id)

SELECT
    department,
    employee,
    salary
FROM merged
WHERE rank <= 3;

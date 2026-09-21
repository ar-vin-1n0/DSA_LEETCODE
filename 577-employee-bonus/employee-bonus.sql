-- Write your PostgreSQL query statement below
SELECT name,bonus FROM Employee
left JOIN Bonus on Employee.empId = bonus.empId
WHERE bonus < 1000 or bonus IS NULL;
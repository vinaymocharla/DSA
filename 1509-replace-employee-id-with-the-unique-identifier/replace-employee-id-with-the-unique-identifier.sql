# Write your MySQL query statement below


SELECT unique_id,name FROM Employees
LEFT JOIN employeeuni ON Employees.id=employeeuni.id
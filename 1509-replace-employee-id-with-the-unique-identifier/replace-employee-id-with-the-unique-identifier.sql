# Write your MySQL query statement below


SELECT Euni.unique_id,E.name FROM Employees E
LEFT JOIN Employeeuni Euni ON E.id=Euni.id
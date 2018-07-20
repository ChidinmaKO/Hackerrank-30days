SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code), COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
FROM company c
JOIN lead_manager l
ON l.company_code = c.company_code
JOIN senior_manager s
ON s.lead_manager_code = l.lead_manager_code
JOIN manager m
ON m.senior_manager_code = s.senior_manager_code
JOIN employee e
ON e.manager_code = m.manager_code
GROUP BY 1, 2
ORDER BY 1;

--OR

SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code), COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
FROM company c, lead_manager l, senior_manager s, manager m, employee e
WHERE l.company_code = c.company_code AND s.lead_manager_code = l.lead_manager_code AND m.senior_manager_code = s.senior_manager_code AND e.manager_code = m.manager_code
GROUP BY 1, 2
ORDER BY 1;

--mysql & oracle

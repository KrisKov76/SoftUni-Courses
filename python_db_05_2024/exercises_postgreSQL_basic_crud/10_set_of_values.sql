SELECT
	employee_id,
	project_id
FROM
	employees_projects
WHERE
	employee_id IN (200, 250)
	    AND
	project_id NOT IN (50, 100);

--тук използваме IN и NOT IN операторите за включване и изключване на конкретни стойности
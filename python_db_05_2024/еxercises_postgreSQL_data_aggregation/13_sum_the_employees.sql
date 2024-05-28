    SELECT
        COUNT(CASE department_id WHEN 1 THEN 1 ELSE NULL END) "Engineering",
        COUNT(CASE department_id WHEN 2 THEN 1 ELSE NULL END) "Tool_Design",
        COUNT(CASE department_id WHEN 3 THEN 1 ELSE NULL END) "Sales",
        COUNT(CASE department_id WHEN 4 THEN 1 ELSE NULL END) "Marketing",
        COUNT(CASE department_id WHEN 5 THEN 1 ELSE NULL END) "Purchasing",
        COUNT(CASE department_id WHEN 6 THEN 1 ELSE NULL END) "Research_and_Development",
        COUNT(CASE department_id WHEN 7 THEN 1 ELSE NULL END) "Production"
    FROM
        employees
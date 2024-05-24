SELECT
	id,
	CONCAT (first_name,	' ', last_name) AS full_name,
	job_title
FROM
    employees
ORDER BY
    first_name
LIMIT 50

--ВЗЕМИ
--    id,
--    конкатинираните
--    (first_name, '', last_name) КАТО full_name,
--    job_title
--OT employees
--като ги ПОДРЕДИШ по first_name
--и ги ЛИМИТИРАШ до 50




SELECT
	id,
	CONCAT_WS (' ', first_name,	 middle_name, last_name) AS full_name,
	hire_date
FROM
    employees
OFFSET 9

--Тук използваме OFFSET (отместване), за да покаже редовете от 10-тия нататък
--За първи път използваме и CONTAT_WS, за да сложи разделител автоматично между имената
-- CONCAT_WS (concat with separator)

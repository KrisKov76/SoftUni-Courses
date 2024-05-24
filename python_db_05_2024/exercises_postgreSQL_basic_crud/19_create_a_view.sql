CREATE VIEW
	view_company_chart
AS
SELECT
	full_name,
	job_title
FROM
	company_chart

WHERE
	manager_id = 184;

--тук съобразяваме, че има таблица company_chart, която трябва да използваме и че
--full_name си е част от таблицата и трябва да се използва
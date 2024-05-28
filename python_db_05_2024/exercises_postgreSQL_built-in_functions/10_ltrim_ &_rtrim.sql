SELECT
	LTRIM(peak_name, 'M') AS "left_trim",
	RTRIM(peak_name, 'm') AS "right_trim"
FROM peaks;

--LTRIM и RTRIM маха не само спейсове (по подразбиране), може да маха стрингове (отляво и отдясно)!


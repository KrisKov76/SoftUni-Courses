SELECT
	continent_name,
	LTRIM(continent_name) AS trim
	TRIM(LEADING FROM continent_name) AS "trim"
FROM continents;

SELECT
	continent_name,
	TRIM(LEADING FROM continent_name) AS "trim"
FROM continents;

--- TRIM маха (реже) празните пространства от двете страни, а LTRIM (маха вляво); RTRIM (маха вдясно)
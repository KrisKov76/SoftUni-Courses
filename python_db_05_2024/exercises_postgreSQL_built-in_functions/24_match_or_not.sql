SELECT
	companion_full_name,
	email
FROM
	users
WHERE
	companion_full_name ILIKE '%and%'
		AND
	email NOT LIKE '%@gmail' -- sasho@gmail - not valid; sasho@gmail.com - valid cause not ending gmail
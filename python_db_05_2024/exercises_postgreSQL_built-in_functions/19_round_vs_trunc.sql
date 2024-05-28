--SELECT
--    TRUNC(5.56777, 2),
--    ROUND(5.55555, 2)
--
--5.56 - TRUNC реже числата, без да закръгля
--5.57 - ROUND гледа следващите числа и закръгля (от 5 закръгля нагоре, до 5 закръгля надолу)

SELECT
	latitude,
	ROUND(latitude, 2),
	TRUNC(latitude, 2)
FROM
	apartments;

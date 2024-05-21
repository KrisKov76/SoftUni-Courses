SELECT
	DISTINCT ON (name)
	name,
	area AS area_km2
FROM cities
ORDER BY name DESC;

--Избери
--    как (без дупликати) чрез DISTINCT ON (на имена)
--    какво
--    name
--    area като area_km2
--от cities
--подредени по name как DESC в низходящ ред

-- ON пишем, когато селектираме само определена колона, в случая name

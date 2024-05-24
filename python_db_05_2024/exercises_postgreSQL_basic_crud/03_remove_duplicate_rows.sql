SELECT
	DISTINCT ON (name)
	name,
	area AS area_km2
FROM
    cities
ORDER BY name DESC;

--ВЗЕМИ
--    как (без дупликати) чрез DISTINCT ON (на имена)
--    name
--    area като area_km2
--ОТ cities
--подредени по name как DESC в низходящ ред

-- ON пишем, когато селектираме само определена колона, в случая name

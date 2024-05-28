SELECT
	(REGEXP_MATCHES("River Information", '([0-9]{1,4})'))[1] AS river_length
FROM view_river_info

-- тъй като REGEXP_MATCHES връща списък от 2 съвпадения (за 4-цифреното число и още едно едноцифрено число),
-- допълваме регекса с [1], за да вземем първото съвпадение от двете, в случая 4-цифреното число
-- [1] маха и скобите, така че да останат само числата

SELECT
	SUBSTRING("River Information", '[0-9]{1,4}') AS river_length
FROM view_river_info

--SUBSTRING поддържа регекс, но само за първо съвпадение, за второ и т.н. се използва регекса


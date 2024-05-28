SELECT
	capital,
    TRANSLATE(capital,'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM
	countries;

--TRANSLATE променя символ по символ, както и дума по дума


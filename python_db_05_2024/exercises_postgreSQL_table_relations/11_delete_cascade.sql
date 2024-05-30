ALTER TABLE
	countries

ADD CONSTRAINT
	fk_countries_contitents
FOREIGN KEY (continent_code) REFERENCES continents(continent_code)
ON DELETE CASCADE,

ADD CONSTRAINT
	fk_countries_currencies
FOREIGN KEY (currency_code) REFERENCES currencies(currency_code)
ON DELETE CASCADE;

-- SELECT * FROM countries WHERE continent_code = 'EU';
-- DELETE FROM continents WHERE continent_code = 'EU'

SELECT MAX(age) as maximum_age
FROM wizard_deposits
-- или

SELECT age as maximum_age
FROM wizard_deposits
ORDER BY age DESC
LIMIT 1
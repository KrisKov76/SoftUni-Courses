SELECT MIN(deposit_charge) as minimum_deposit_charge
FROM wizard_deposits
-- или

SELECT deposit_charge as minimum_deposit_charge
FROM wizard_deposits
ORDER BY deposit_charge ASC
LIMIT 1
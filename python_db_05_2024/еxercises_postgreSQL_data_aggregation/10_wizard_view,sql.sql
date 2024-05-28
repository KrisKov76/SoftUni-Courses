CREATE OR REPLACE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17 AS
SELECT
    CONCAT(w.first_name, ' ', w.last_name) AS wizard_name,
    w.deposit_start_date AS start_date,
    w.deposit_expiration_date AS expiration_date,
    w.deposit_amount AS amount
FROM
    wizard_deposits w
WHERE
    w.deposit_expiration_date <= '1983-08-17'
GROUP BY
	wizard_name, deposit_start_date, deposit_expiration_date, deposit_amount
ORDER BY
	expiration_date ASC
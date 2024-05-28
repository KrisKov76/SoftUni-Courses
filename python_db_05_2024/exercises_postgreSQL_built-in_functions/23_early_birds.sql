 SELECT
	user_id,
	AGE(starts_at, booked_at) AS early_birds
FROM
	bookings
WHERE
	starts_at - booked_at >= '10 MONTHS'

-- изваждане на дати една от друга с AGE
-- внимаваме да вадим от по-новата дата, по-старата, за да не получим отрицателно число

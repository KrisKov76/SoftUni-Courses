DELETE FROM
	addresses
WHERE
	city_id IN (5, 17, 20, 30)

--Обръщам внимание, че се пише: DELETE FROM и пишем откъде трием, от коя таблица
--Може да сложим накрая RETURNING *, за да видим какво сме изтрили
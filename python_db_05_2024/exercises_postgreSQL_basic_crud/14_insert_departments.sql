INSERT INTO
	departments (department, manager_id)
VALUES
	('Finance', 3),
	('Information Services', 42),
	('Document Control', 90),
	('Quality Assurance', 274),
	('Facilities and Maintenance', 218),
	('Shipping and Receiving', 85),
	('Executive', 109);
RETURNING *;

--SELECT
--	department,
--	manager_id
--FROM
--	departments

преди SELECT може да напишем RETURNING *, за да видим дали успешно сме insert-нали данните


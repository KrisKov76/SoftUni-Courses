--Retrieve all projects without an "end_date" - означава на които датата е NULL

--трябва да ъпдейтнеш проектите, които нямат крайна дата - end_date IS NULL
--като крайната дата е началната + 5 месеца - SET end_date = start_date + INTERVAL '5 months'

UPDATE
    projects
SET
    end_date = start_date + INTERVAL '5 months'
WHERE
	end_date IS NULL

--или друг пример (не е задача)
UPDATE
    test
SET
    mood = 'happy'
WHERE
    mood = NULL
RETURNING *;


CREATE TABLE minions (
	id serial PRIMARY KEY,
	name VARCHAR(30),
	age int
)


CREATE TABLE IF NOT EXISTS minions (
	id serial PRIMARY KEY,
	name VARCHAR(30),
	age INTEGER
)
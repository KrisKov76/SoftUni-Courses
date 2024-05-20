ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20),
ADD COLUMN equipped BOOLEAN NOT NULL;

--за да бъде TRUE или False се изисква да е BOOLEAN NOT NULL

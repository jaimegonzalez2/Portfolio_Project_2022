# This is a SQL project from CodeCademy on how to create a table and manipulate it with information. 

CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30')

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Albie G', '2001-03-12')

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Daisy G', '2020-01-01')

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'email1@email.com'
WHERE id = 2;

DELETE FROM friends
WHERE id = 1;

SELECT *
FROM friends;

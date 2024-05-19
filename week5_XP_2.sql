create table students(
	student_id serial primary key,
	first_name varchar (50) not null,
	last_name varchar (100) not null,
	birth_date date not null
);
INSERT INTO students (first_name, last_name,birth_date)
VALUES
    ('Marc', 'Benichou','1998-11-02'),
    ('Yoan', 'Cohen','2010-12-03'),
	('Lea', 'Benichou', '1987-07-27'),
	('Amelia','Dux','1996-04-07'),
	('David', 'Grez','2003-06-14'),
	('Omer','Simpson','1980-10-03');
INSERT INTO students('first_name', 'last_name','birth-day')
VALUES ('Alexander','Luzhkov','1966-04-14');

SELECT * FROM students;
SELECT first_name, last_name FROM students;
SELECT first_name, last_name FROM students WHERE student_id = 2;
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_';
SELECT first_name, last_name FROM students WHERE student_id IN (1, 3);
SELECT * FROM students WHERE birth_date >= '2000-01-01';


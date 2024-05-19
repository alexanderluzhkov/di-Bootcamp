create table items(
	items_id SERIAL PRIMARY KEY,
	name_item VARCHAR (50) not null,
	price NUMERIC (10) not null
);
create table customers(
	cusromers_id serial primary key,
	first_name varchar (50) not null,
	last_name varchar (100) not null
);
INSERT INTO items (name_item, price)
VALUES
    ('small desk', 100),
    ('large desk', 300),
	('fan', 80);
INSERT INTO customers (first_name, last_name)
VALUES
    ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
	('Scott', 'Scott'),
	('Trevor','Green'),
	('Melany', 'Johnson');
select * from customers;
select * from items
where price > 80;
select * from items
where price <= 300;
select * from customers
where last_name = 'Smith';
select * from customers
where last_name = 'Jones';
select * from customers
where first_name != 'Scott';






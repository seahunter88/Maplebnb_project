# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a Maplebnb user, 
I want to create a new space,
So that users can book it.
As a Maplebnb user,
I want to be able create an account,
So that I can make booking and listings.

```

```
Nouns:

user, space, account, booking, listings.
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| user                  | id, username, password
| space                 | id, title, price, description

1. Name of the first table (always plural): `users` 

    Column names: `username`, `password`

2. Name of the second table (always plural): `space` 

    Column names: `title, price, description`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
username: VARCHAR(255)
password: VARCHAR(255)

Table: space
id: SERIAL
title: VARCHAR(255)
price: int
description: VARCHAR(255)
user_id: int
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [user] have many [space]? (Yes)
2. Can one [space] have many [user]? (No)

You'll then be able to say that:

1. **[User] has many [spaces]**
2. And on the other side, **[space] belongs to [user]**
3. In that case, the foreign key is in the table [space] :)

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one user have many users? YES
2. Can one space have many space? NO

-> Therefore,
-> An user HAS MANY users
-> An space BELONGS TO an user

-> Therefore, the foreign key is on the users table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: users_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

-- Then the table with the foreign key second.
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  price int,
  description VARCHAR(255),
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < users_table.sql
```
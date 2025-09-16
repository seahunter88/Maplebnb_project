DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;


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

INSERT INTO users (username, password) VALUES ('Sarahmonster9000', 'Iloveponies!');
INSERT INTO users (username, password) VALUES ('HunoristheGOAT', 'Pokemon$');

INSERT INTO spaces (title, price, description, user_id) VALUES ('House_1', '100', 'a nice house', 1);
INSERT INTO spaces (title, price, description, user_id) VALUES ('House_2', '150', 'a nicer house', 1);

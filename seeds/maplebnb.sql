DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  price int,
  description VARCHAR(255),
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  booking_date date,
  space_id int,
  booking_user_id int,
  constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade,
  constraint fk_booking_user foreign key(booking_user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (username, password) VALUES ('Sarahmonster9000', 'Iloveponies!');
INSERT INTO users (username, password) VALUES ('HunoristheGOAT', 'Pokemon$');

INSERT INTO spaces (title, price, description, user_id) VALUES ('House_1', '100', 'a nice house', 1);
INSERT INTO spaces (title, price, description, user_id) VALUES ('House_2', '150', 'a nicer house', 1);

INSERT INTO bookings (booking_date, space_id, booking_user_id) VALUES ('2025-09-17', 1, 1);
INSERT INTO bookings (booking_date, space_id, booking_user_id) VALUES ('2025-08-17', 2, 2);

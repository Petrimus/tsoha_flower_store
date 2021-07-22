CREATE TABLE flower_user (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR (20) NOT NULL,
  last_name VARCHAR (30) NOT NULL,
  username VARCHAR (25) NOT NULL unique,
  user_email VARCHAR (100) NOT NULL unique,
  password VARCHAR (32) NOT NULL,
  is_admin BOOlean DEFAULT FALSE,
  created_at TIMESTAMP
  );

CREATE TABLE adress (
  street_and_nro TEXT NOT NULL,
  postal_code INTEGER NOT NULL,
  city TEXT NOT NULL,
  country TEXT NOT NULL,
  created_at TIMESTAMP,
  flower_user_id INTEGER REFERENCES flower_user(flower_user_id)
);

CREATE TABLE creditcard (
  id SERIAL PRIMARY KEY,
  experience_date Date NOT NULL,
  card_number Integer NOT NULL,
  created_at TIMESTAMP,
  flower_user_id INTEGER REFERENCES flower_user(flower_user_id)
  );

CREATE TABLE flower (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  latin_name TEXT NOT NULL,
  description TEXT NOT NULL,
  price NUMERIC NOT NULL,
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE inventory (
  id SERIAL PRIMARY KEY,
  quantity Integer NOT NULL,
  last_replenished DATE,
  next_replenish DATE
);

CREATE TABLE shoppingcart (
  id SERIAL PRIMARY KEY,
  status Integer references shoppingcart_status(id)
  name VARCHAR (30) NOT NULL,
  user_id INTeger(10) DEFAULT NULL,
  total NUMERIC (10) NOT NULL DEFAULT '0.00',
  status INT references shoppingcart_status(id)
  created_at TIMESTAMP NOT NULL,
  modified_at` TIMESTAMP
);

CREATE TABLE shoppingcart_item (
  id SERIAL PRIMARY KEY,
  quantity INTEGER DEFAULT 0 NOT NULL,
  created_at TIMESTAMP NOT NULL,
  modified_at` TIMESTAMP

);

CREATE TABLE shoppingcart_status (
   id SERIAL PRIMARY KEY,
   info TEXT,
   status VARCHAR (10) NOT NULL,
   created_at DATE,
   modified_at Date
)
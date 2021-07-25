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
  id SERIAL PRIMARY KEY,
  street_and_nro TEXT NOT NULL,
  postal_code INTEGER NOT NULL,
  city TEXT NOT NULL,
  country TEXT NOT NULL,
  created_at TIMESTAMP,
  flower_user_id INTEGER REFERENCES flower_user
);

CREATE TABLE creditcard (
  id SERIAL PRIMARY KEY,
  experience_date Date NOT NULL,
  card_number Integer NOT NULL,
  created_at TIMESTAMP,
  flower_user_id INTEGER REFERENCES flower_user
  );


CREATE TABLE messages (id SERIAL PRIMARY KEY, content TEXT);

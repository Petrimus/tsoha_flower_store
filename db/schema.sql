CREATE TABLE flower_user (
  id SERIAL PRIMARY KEY,  
  first_name VARCHAR (20) NOT NULL,
  last_name VARCHAR (30) NOT NULL,  
  username VARCHAR (100) NOT NULL unique,
  password VARCHAR NOT NULL,
  is_admin BOOlean DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
  );

CREATE TABLE adress (
  id SERIAL PRIMARY KEY,
  street_and_nro TEXT NOT NULL,
  postal_code INTEGER NOT NULL,
  city TEXT NOT NULL,  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  flower_user_id INTEGER REFERENCES flower_user
);

CREATE TABLE creditcard (
  id SERIAL PRIMARY KEY,
  experience_date Date NOT NULL,
  card_number Integer NOT NULL,
  created_at TIMESTAMP,
  flower_user_id INTEGER REFERENCES flower_user
  );

CREATE TABLE flower (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  latin_name TEXT NOT NULL,
  description TEXT NOT NULL,
  price NUMERIC NOT NULL,
  picture TEXT NOT NULL,
  picture_alt TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE inventory (
  id SERIAL PRIMARY KEY,
  quantity Integer NOT NULL,
  last_restock DATE,
  next_restock DATE,
  flower_id INTEGER REFERENCES flower
);

CREATE TABLE shoppingcart_status (
   id SERIAL PRIMARY KEY,
   status_text TEXT NOT NULL    
);

CREATE TABLE shoppingcart (
  id SERIAL PRIMARY KEY,   
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  modified_at TIMESTAMP,
  status_id INTEGER REFERENCES shoppingcart_status,
  flower_user_id INTEGER REFERENCES flower_user  
);

CREATE TABLE shoppingcart_item (
  id SERIAL PRIMARY KEY,
  quantity INTEGER DEFAULT 1 NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  flower_id INTEGER REFERENCES flower,
  shoppingcart_id INTEGER REFERENCES shoppingcart
);

CREATE TABLE messages (id SERIAL PRIMARY KEY, content TEXT);

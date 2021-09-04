INSERT INTO messages (content) VALUES ('apina banaani cembalo');
INSERT INTO flower_user (first_name, last_name, username, password, is_admin) VALUES ('Test', 'Tester', 'test@tester.io', 'pbkdf2:sha256:260000$eIbz9ILN0n2VzrqN$6ba81ef688883c0660e4879ec5fa625229c80ec9f02d85ec10ee1c8577a05a7a', True);
INSERT INTO flower (name, latin_name, description, price, picture, picture_alt, created_at) VALUES ('Marigold', 'Tagetes', 'Highly fragrant and heat tolerant marigolds are popular and durable summer flowers. Marigolds are also suitable for decorating the vegetable garden, as they act as a repellent for pests. There are hundreds of varieties.', 1.10, '/static/images/samettikukka.jpg', 'samettikukka', '2021-06-22 19:10:25-07');
INSERT INTO flower (name, latin_name, description, price, picture, picture_alt, created_at) VALUES ('Dahlia', 'Dahlia x hortensis', 'The Dahlia is a traditional summer flower that blooms glowing in late summer. Dalia''s variety is varied. Flower shapes range from spherical to daisy-like and the color range covers almost all colors.', 3.50, '/static/images/daalia.jpg', 'daalia', '2021-06-22 19:10:25-07');
INSERT INTO flower (name, latin_name, description, price, picture, picture_alt, created_at) VALUES ('Water Lilly', 'Nymphaea', 'Water lilies are aquatic plants. Their ground stem and root system grow buried at the bottom of a lake or bay. The long-stemmed leaves and flower buds of water lilies extend to the surface of the water.', 2.50, '/static/images/lumme.jpg', 'lumme', '2021-06-22 19:10:25-07');
INSERT INTO flower (name, latin_name, description, price, picture, picture_alt, created_at) VALUES ('Geranium', 'Pelargonium', 'The genus of geraniums includes a wide variety of potted plants, herbs, sparrow plants and shrubs, each with its own unique growth pattern and appearance.', 3.75, '/static/images/pelargonia.jpg', 'pelargonia', '2021-06-22 19:10:25-07');
INSERT INTO flower (name, latin_name, description, price, picture, picture_alt, created_at) VALUES ('Verbena', 'Verbena', 'Verbena is an easy-care and vigorous pot and ampoule plant that can withstand even low temperatures.', 0.90, '/static/images/rautayrtti.jpg', 'rautayrtti', '2021-06-22 19:10:25-07');
INSERT INTO flower (name, latin_name, description, price, picture, picture_alt, created_at) VALUES ('Rose', 'Loise Bugnet', 'Beautiful daisy. Strong and bushy and almost thornless vegetation. The reddish buds peel a white fragrant flower. Thrives from the sun to the semi-shade, even in a low-nutrient country.', 6.80, '/static/images/ruusu.jpg', 'ruusu', '2021-06-22 19:10:25-07');
INSERT INTO inventory (quantity, last_restock, next_restock, flower_id) VALUES (13, '2021-06-22 19:10:25-07', '2021-06-29 19:10:25-07', 1);
INSERT INTO inventory (quantity, last_restock, next_restock, flower_id) VALUES (21, '2021-06-22 19:10:25-07', '2021-06-29 19:10:25-07', 2);
INSERT INTO inventory (quantity, last_restock, next_restock, flower_id) VALUES (10, '2021-06-22 19:10:25-07', '2021-06-29 19:10:25-07', 3);
INSERT INTO inventory (quantity, last_restock, next_restock, flower_id) VALUES (54, '2021-06-22 19:10:25-07', '2021-06-29 19:10:25-07', 4);
INSERT INTO inventory (quantity, last_restock, next_restock, flower_id) VALUES (32, '2021-06-22 19:10:25-07', '2021-06-29 19:10:25-07', 5);
INSERT INTO inventory (quantity, last_restock, next_restock, flower_id) VALUES (45, '2021-06-22 19:10:25-07', '2021-06-29 19:10:25-07', 6);
INSERT INTO shoppingcart_status (status_text) VALUES ('open'), ('ordered'), ('completed'), ('deleted'); 
INSERT INTO shoppingcart (created_at, status_id, flower_user_id) VALUES ('2021-06-22 19:10:25-07', 1, 1);
INSERT INTO shoppingcart_item (quantity, flower_id, shoppingcart_id) VALUES (2, 1, 1);
INSERT INTO shoppingcart_item (quantity, flower_id, shoppingcart_id) VALUES (3, 2, 1);
INSERT INTO shoppingcart_item (quantity, flower_id, shoppingcart_id) VALUES (4, 3, 1);
INSERT INTO shoppingcart_item (quantity, flower_id, shoppingcart_id) VALUES (5, 5, 1);
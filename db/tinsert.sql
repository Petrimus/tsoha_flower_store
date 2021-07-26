INSERT INTO messages (content) VALUES ('apina banaani cembalo');
INSERT INTO flower_user (first_name, last_name, username, user_email, password, is_admin) VALUES ('Petri', 'Palmu', 'palmupe', 'petri@mikalie.io', 'petri', True);
INSERT INTO flower (name, latin_name, description, price, created_at) VALUES ('Samettikukka', 'Tagetes', 'Voimakkaasti tuoksuvat ja paahdetta sietävät samettikukat ovat suosittuja ja kestäviä kesäkukkia. Samettikukat sopivat myös kasvimaan koristukseksi, sillä ne toimivat tuholaisten karkotuskasvina. Lajikkeita on satoja erilaisia.', 1.10, '2021-06-22 19:10:25-07');
INSERT INTO inventory (quantity, last_restock, next_restock, flower_id) VALUES (5, '2021-06-22 19:10:25-07', '2021-06-29 19:10:25-07', 1);
INSERT INTO shoppingcart_status (info, status) VALUES ('Your order is completed and it is on delivery', 'completed');
INSERT INTO shoppingcart (name, created_at, status_id, flower_user_id) VALUES ('first cart', '2021-06-22 19:10:25-07', 1, 1);
INSERT INTO shoppingcart_item (flower_id, shoppingcart_id) VALUES (1, 1);
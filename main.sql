CREATE TABLE resource (id int, module_id macaddr, type varchar, value varchar, sent_at timestamp);
CREATE TABLE devices (id int, module_id macaddr, allowed_users varchar);
CREATE TABLE users (id int, username varchar, password varchar, email varchar, display_name varchar, created_at timestamp, locked boolean, banned boolean);
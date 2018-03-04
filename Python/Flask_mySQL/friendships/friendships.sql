-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- 	VALUE("CHRIS", "BAKER", DATE("2018-02-12"), DATE("2018-02-12"));
-- 
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- 	VALUE("JESSICA", "DAVIDSON", DATE("2018-02-12"), DATE("2018-02-12"));
--     
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- 	VALUE("JAMES", "JOHNSON", DATE("2018-02-12"), DATE("2018-02-12"));
--     
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- 	VALUE("DIANA", "SMITH", DATE("2018-02-12"), DATE("2018-02-12"));


SELECT users.first_name, users.last_name FROM users 
LEFT JOIN friendships ON users.id = friendships.users_id




-- LEFT JOIN users as user2 ON ____ = ____
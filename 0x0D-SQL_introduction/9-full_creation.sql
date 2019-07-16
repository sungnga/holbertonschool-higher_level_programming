-- A script that creates a table second_table in the database hbtn_0c_0
-- in your MySQL server and add multiples rows
CREATE TABLE [IF NOT EXISTS] second_table (id INT,
name VARCHAR(256),
score INT);

INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (NULL, 'John', '10');
INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (NULL, 'Alex', '3');
INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (NULL, 'Bob', '14');
INSERT INTO `second_table` (`id`,`name`,`score`) VALUE (NULL, 'George', '8');

create DATABASE mdm_db;
use mdm_db;
CREATE TABLE documents (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,title VARCHAR(30) NOT NULL,heading VARCHAR(30) NOT NULL,body VARCHAR(100),date TIMESTAMP);
insert into documents values (2,'title2','heading2','body2',NOW());
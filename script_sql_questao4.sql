CREATE DATABASE sales_banco_de_dados;
USE sales_banco_de_dados;

CREATE TABLE pedidos (
    cliente_id INT,
    email VARCHAR(255),
    telefone VARCHAR(50),
    endereco VARCHAR(255),
    numero VARCHAR(50),
    nome_sobrenome VARCHAR(255),
    order_id INT,
    product_name VARCHAR(255),
    quantity INT,
    unit_price DECIMAL(10, 2),
    order_date DATE
);
-- Verificando o diretório permitido
SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\combined_customer_sales_data.csv'
INTO TABLE pedidos
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cliente_id, email, telefone, endereco, numero, nome_sobrenome, order_id, product_name, quantity, unit_price, @order_date)
SET order_date = STR_TO_DATE(@order_date, '%d/%m/%Y');


SELECT 
    product_name,
    SUM(quantity * unit_price) AS total_sales
FROM 
    pedidos
GROUP BY 
    product_name
ORDER BY 
    total_sales DESC;


SELECT 
    cliente_id,
    COUNT(order_id) AS total_orders
FROM 
    pedidos
GROUP BY 
    cliente_id
ORDER BY 
    total_orders DESC;

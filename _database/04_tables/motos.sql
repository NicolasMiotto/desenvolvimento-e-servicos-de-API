CREATE DATABASE IF NOT EXISTS db_motos;
USE db_motos;

DROP TABLE IF EXISTS motos;

-- Tabela com 7 colunas (conforme exigido na instrução)
CREATE TABLE motos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    cilindrada INT NOT NULL,
    cor VARCHAR(30) NOT NULL,
    ano INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

-- Carga inicial para testes
INSERT INTO motos (marca, modelo, cilindrada, cor, ano, preco) VALUES
('Honda', 'CB 500F', 500, 'Vermelho', 2023, 39100.00),
('Yamaha', 'MT-07', 689, 'Preto', 2024, 46990.00),
('Kawasaki', 'Ninja 400', 399, 'Verde', 2022, 34800.00),
('BMW', 'F 850 GS', 853, 'Cinza', 2023, 74500.00),
('Ducati', 'Panigale V2', 955, 'Vermelho', 2024, 98900.00),
('Harley-Davidson', 'Iron 883', 883, 'Preto Fosco', 2021, 55000.00),
('Triumph', 'Street Triple 765', 765, 'Branco', 2023, 59990.00),
('Suzuki', 'GSX-S750', 749, 'Azul', 2022, 53200.00),
('Royal Enfield', 'Meteor 350', 349, 'Amarelo', 2023, 21790.00),
('KTM', '390 Duke', 373, 'Laranja', 2024, 33990.00);
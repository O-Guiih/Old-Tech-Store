-- CRIAÇÂO DO BANCO DE DADOS
CREATE DATABASE ecommerce_db;
USE ecommerce_db;

-- TABELA DE USUÁRIOS 
CREATE TABLE usuarios ( -- Cria a tabela usuários
	id INT AUTO_INCREMENT PRIMARY KEY, -- ID único automático
    nome VARCHAR(100) NOT NULL, -- Nome de usuário 
    email VARCHAR(100) NOT NULL UNIQUE, -- Email único para login 
    senha VARCHAR(255) NOT NULL -- Senha do usuário
);

-- TABELA DE PRODUTOS
CREATE TABLE produtos (
	id INT AUTO_INCREMENT PRIMARY KEY, -- ID único automático 
    nome VARCHAR(200) NOT NULL, -- Nome do produto 
    preco DECIMAL(10, 2) NOT NULL -- Preço com 2 casas decimais
);

SHOW TABLES; -- Mostra todas as tabelas do banco
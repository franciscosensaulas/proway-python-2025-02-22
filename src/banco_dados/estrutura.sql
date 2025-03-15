DROP DATABASE IF EXISTS lojadb;
CREATE DATABASE lojadb;
USE lojadb;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

-- PRIMARY KEY é a chave primária, ou seja, um identificador único na tabela
-- AUTO_INCREMENT, preenche o id com número sequencial: 1,  2, 3
-- INT usado para campo de número inteiro
-- VARCHAR usado para campo de texto até 100 caracteres neste exemplo
-- NOT NULL faz o campo ser obrigatório

-- Adicionando uma coluna chamada cpf na tabela de clientes
-- O cpf será armazenado como texto, pq pode começar com 0 a esquerda
-- O cpf será armazenado no seguinte formato: '230.291.399-20'
ALTER TABLE clientes ADD COLUMN cpf VARCHAR(14);

SELECT * FROM clientes;
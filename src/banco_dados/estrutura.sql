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

INSERT INTO clientes (nome, cpf) VALUES ('Ana', '123.456.789-10');
INSERT INTO clientes (nome, cpf) VALUES ('Matheus da Silva', '392.129.201-20');

-- NOT NULL é obrigatório
CREATE TABLE pedidos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    produto VARCHAR(100) NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL,

    id_cliente INT NOT NULL,
    -- FOREIGN KEY: Chave estrangeira é a forma que fazemos para relacionar um registro 
    -- a outro, uma FK sempre esta atrelada a uma PK.
    -- O tipo da coluna FK deve ser o mesmo que a coluna PK
    -- Ex. Na tabela de clientes o id(PK) é int, na tabela de pedidos o id_cliente(FK) deve ser int
    FOREIGN KEY(id_cliente) REFERENCES clientes(id),

    -- DATETIME é a coluna utilizada para armazenar data e hora
    -- DEFAULT é utilizado para definir um valor padrão quando n é informado no insert
    -- NOW() é a data e hora atual, ou seja quando executado um insert na tabela de pedidos, 
    --      vai preencher a coluna data_criacao com data e hora atual, para sabermos quando foi realizado aquele pedido
    data_hora_criacao DATETIME DEFAULT NOW()
);

INSERT INTO pedidos (produto, preco_unitario, quantidade, id_cliente) VALUES
('Camisa', 100.00, 5, 1), -- id_cliente 1 é a Ana
('Calça', 170.00, 3, 1), -- pedido para ana
('Tênis', 80.00, 1, 2); -- pedido para o Francisco id_cliente 2

SELECT * FROM clientes;
select * from pedidos;
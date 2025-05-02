from typing import List
from src.banco_dados.conexao import conectar
from src.modelos.cliente import Cliente
from src.modelos.pedido import Pedido

def cadastrar(produto: str, quantidade: int, preco_unitario: float, id_cliente:int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO pedidos (produto, quantidade, preco_unitario, id_cliente) VALUES (%s, %s, %s, %s)",
        (produto, quantidade, preco_unitario, id_cliente)
    )
    conexao.commit()
    conexao.close()


def editar(id_pedido: int, quantidade: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE pedidos SET quantidade = %s WHERE id = %s", (quantidade, id_pedido))
    conexao.commit()
    
    quantidade_linhas_afetadas = cursor.rowcount
    conexao.close()

    return quantidade_linhas_afetadas



def obter_todos() -> List[Pedido]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""

SELECT 
	pedidos.id,
    pedidos.produto,
    pedidos.quantidade,
    pedidos.preco_unitario,
    pedidos.id_cliente,
    clientes.nome
    FROM pedidos
    inner join clientes on (pedidos.id_cliente = clientes.id);
""")
    registros = cursor.fetchall()
    conexao.close()

    pedidos  = []

    for registro in registros:
        id_pedido = registro[0]
        produto = registro[1]
        quantidade = registro[2]
        preco_unitario = registro[3]
        id_cliente = registro[4]
        nome_cliente = registro[5]

        pedido = Pedido()
        pedido.id = int(id_pedido)
        pedido.produto = produto
        pedido.quantidade = int(quantidade)
        pedido.preco_unitario = float(preco_unitario)

        pedido.cliente = Cliente()
        pedido.cliente.id = int(id_cliente)
        pedido.cliente.nome = nome_cliente

        pedidos.append(pedido)
        
    return pedidos


def obter_por_id(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT 
	pedidos.id,
    pedidos.produto,
    pedidos.quantidade,
    pedidos.preco_unitario,
    pedidos.id_cliente,
    clientes.nome
    FROM pedidos
    inner join clientes on (pedidos.id_cliente = clientes.id)
    WHERE pedidos.id = %s""", (id,))
    pedido = cursor.fetchone()
    pedido = {
        "id": int(pedido[0]),
        "produto": pedido[1],
        "quantidade": int(pedido[2]),
        "preco_unitario": int(pedido[3]),
        "id_cliente": int(pedido[4]),
        "nome_cliente": pedido[5] 
    }
    return pedido


def apagar(id_pedido: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM pedidos WHERE id = %s", (id_pedido,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    return linhas_afetadas

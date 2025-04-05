from src.banco_dados.conexao import conectar


def cadastrar(nome: str, cpf: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
    conexao.commit()
    conexao.close()

def editar(nome:str, cpf:str, idEditar:int) -> int:
    conexao = conectar()
    # UPDATE clientes SET nome='Oscar' WHERE id = 5
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET nome=%s, cpf=%s WHERE id=%s", (nome, cpf, idEditar))
    conexao.commit()
    quantidade_afetadas = cursor.rowcount
    conexao.close()

    return quantidade_afetadas 

def obter_todos():
    conexao = conectar()
    cursor = conexao.cursor()
    # definir qual comande será executado, neste caso buscar os registros cadastrados 
    # na tabela de clientes
    cursor.execute("SELECT id, nome, cpf FROM clientes")
    # executar a consulta, buscando todos os registros de acordo com o SELECT
    registros = cursor.fetchall()
    # fechar a conexão com o bd
    conexao.close()
    return registros

def obter_por_id():
    pass

def apagar(codigo_apagar: int) -> int:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (codigo_apagar,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    conexao.close()
    return linhas_afetadas


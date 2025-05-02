from mysql.connector.pooling import connect, PooledMySQLConnection


# O método conectar irá realizar uma conexão com o banco de dados e retornar a conexão para 
# o lugar que chamou o método conectar
def conectar() -> PooledMySQLConnection:
    conexao = connect(
        host="127.0.0.1",
        password="admin",
        port=3306,
        user="root",
        database="lojadb"
    )
    return conexao

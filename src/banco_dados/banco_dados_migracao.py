import mysql
import mysql.connector


def migrar():
    if existe_banco_dados():
        return


def __abrir_conexao():
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        port=port,
        password=password
    )

def existe_banco_dados():

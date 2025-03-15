import mysql.connector
import questionary
from src.helpers.tela import limpar_tela
import re # importar para trabalhar com expressão regular

# CRUD
# Create - Criar um registro - INSERT INTO nome_tabela (campos) VALUES (valores)
# Read - Consultar registros - SELECT campos FROM nome_tabela
# Update - Atualizar um registro - UPDATE nome_tabela campo=valor, campo2=valor2 WHERE id = valorId
# Delete - Apagar um registro - DELETE FROM nome_tabela WHERE id = valorId

cpf_regex = r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"

def validar_cpf(cpf: str):
    if re.match(cpf_regex, cpf):
        return True
    return "CPF inválido! Digite no seguinte formato: 000.000.000-00"

def validar_nome(nome: str):
    nome = nome.strip() # remover espaços do começo e do fim
    if len(nome) < 3:
        return "O nome deve conter no mínimo 3 caracteres"
    
    if len(nome) > 100:
        return "O nome deve conter no máximo 100 caracteres"
    
    return True # O nome é válido


def cadastrar_cliente():
    nome = questionary.text("Digite o nome do cliente: ", validate=validar_nome).ask().strip()
    cpf = questionary.text("Digite o cpf:", validate=validar_cpf).ask()

    conexao = mysql.connector.connect(
        host="127.0.0.1", # 127.0.0.1 (localhost), ou seja, vai conectar no banco de dados local
        user="root",
        password="admin",
        port=3306,
        database="lojadb"
    )
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
    conexao.commit()
    conexao.close()
    print("Cliente cadastrado com sucesso")

def listar_clientes():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="admin",
        database="lojadb"
    )
    cursor = conexao.cursor()
    # definir qual comande será executado, neste caso buscar os registros cadastrados 
    # na tabela de clientes
    cursor.execute("SELECT id, nome, cpf FROM clientes")
    # executar a consulta, buscando todos os registros de acordo com o SELECT
    registros = cursor.fetchall()
    # fechar a conexão com o bd
    conexao.close()

    print("Lista de clientes:")
    for registro in registros:
        print("Código:", registro[0])
        print("Nome:", registro[1])
        print("CPF:", registro[2], end="\n\n")

def editar_cliente():
    idEditar = int(questionary.text("Digite o código para editar:").ask())
    nome = questionary.text("Digite o nome do cliente:", validate=validar_nome).ask().strip()
    cpf = questionary.text("Digite o cpf do cliente:", validate=validar_cpf).ask()

    # UPDATE clientes SET nome='Oscar' WHERE id = 5
    conexao = mysql.connector.connect(
        host=" 127.0.0.1",
        user="root",
        password="admin",
        port=3306,
        database="lojadb"
    )
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET nome=%s, cpf=%s WHERE id=%s", (nome, cpf, idEditar))
    conexao.commit()
    quantidade_afetadas = cursor.rowcount
    conexao.close()

    if quantidade_afetadas == 1:
        print("Cliente atualizado com sucesso")
    else:
        print("Não encontrado cliente com o código " + str(idEditar))

def apagar_cliente():
    codigo_apagar = int(questionary.text("Digite o código para apagar:").ask())

    conexao = mysql.connector.connect(
        host="127.0.0.1",
        password="admin",
        port=3306,
        user="root",
        database="lojadb"
    )
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (codigo_apagar,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    conexao.close()

    if linhas_afetadas == 1:
        print("Cliente apagado com sucesso")
    else:
        print("Não encontrado cliente com o código " + str(codigo_apagar))

def executar_menu():
    menu_interno = [
        "Listar todos",
        "Cadastrar",
        "Editar",
        "Apagar",
        "Sair"
    ]
    opcao_escolhida = ""

    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
            "Escolha o menu desejado para o Clientes:", 
            choices=menu_interno,
        ).ask()
        limpar_tela()
        
        if opcao_escolhida == "Listar todos":
            listar_clientes()
        elif opcao_escolhida == "Cadastrar":
            cadastrar_cliente()
        elif opcao_escolhida == "Editar":
            editar_cliente()
        elif opcao_escolhida == "Apagar":
            apagar_cliente()
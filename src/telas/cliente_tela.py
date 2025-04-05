import questionary
from src.helpers.tela import limpar_tela
import re

from rich.console import Console
from rich.table import Table

from src.repositorios import cliente_repositorio # importar para trabalhar com expressão regular

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

    cliente_repositorio.cadastrar(nome, cpf)
    
    print("Cliente cadastrado com sucesso")

def listar_clientes():
    registros = cliente_repositorio.obter_todos()

    console = Console()
    tabela = Table(show_lines=True, show_header=True, show_edge=True)
    tabela.add_column(header="Código")
    tabela.add_column(header="Nome")
    tabela.add_column(header="CPF")

    print("Lista de clientes:")
    for cliente in registros:
        tabela.add_row(str(cliente[0]), cliente[1],  cliente[2])
    console.print(tabela)

    # for registro in registros:
    #     print("Código:", registro[0])
    #     print("Nome:", registro[1])
    #     print("CPF:", registro[2], end="\n\n")

def editar_cliente():
    idEditar = int(questionary.text("Digite o código para editar:").ask())
    nome = questionary.text("Digite o nome do cliente:", validate=validar_nome).ask().strip()
    cpf = questionary.text("Digite o cpf do cliente:", validate=validar_cpf).ask()

    quantidade_afetadas = cliente_repositorio.editar(nome, cpf, idEditar)

    if quantidade_afetadas == 1:
        print("Cliente atualizado com sucesso")
    else:
        print("Não encontrado cliente com o código " + str(idEditar))

def apagar_cliente():
    codigo_apagar = int(questionary.text("Digite o código para apagar:").ask())

    linhas_afetadas = cliente_repositorio.apagar(codigo_apagar)

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
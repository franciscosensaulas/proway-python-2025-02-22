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
        tabela.add_row(str(cliente["id"]), cliente["nome"],  cliente["cpf"])
    console.print(tabela)

    # for registro in registros:
    #     print("Código:", registro[0])
    #     print("Nome:", registro[1])
    #     print("CPF:", registro[2], end="\n\n")

def editar_cliente():
    clientes = cliente_repositorio.obter_todos()
    clientes_opcoes = [questionary.Choice(cliente["nome"] + " - " + str(cliente["cpf"]), value=cliente["id"]) 
                       for cliente in clientes]
    
    id_editar = questionary.select("Escolha o cliente para editar:", clientes_opcoes).ask()

    cliente_original = cliente_repositorio.obter_por_id(id_editar)

    nome = questionary.text("Digite o nome do cliente:", validate=validar_nome, default=cliente_original.nome).ask().strip()
    cpf = questionary.text("Digite o cpf do cliente:", validate=validar_cpf, default=cliente_original.cpf).ask()

    quantidade_afetadas = cliente_repositorio.editar(nome, cpf, id_editar)

    if quantidade_afetadas == 1:
        print("Cliente atualizado com sucesso")
    else:
        print("Não encontrado cliente com o código " + str(id_editar))

def apagar_cliente():
    # listar_clientes()
    # codigo_apagar = int(questionary.text("Digite o código para apagar:").ask())
    # print("Código escolhido: ", codigo_apagar)

    clientes = cliente_repositorio.obter_todos()

    # clientes_opcoes = []
    # for cliente in clientes:
    #     opcao = questionary.Choice(cliente["nome"] + " - " + cliente["cpf"], value=cliente["id"])
    #     clientes_opcoes.append(opcao)

    # list comprehension
    clientes_opcoes = [questionary.Choice(cliente["nome"] + " - " + str(cliente["cpf"]), value=cliente["id"]) 
                       for cliente in clientes]
    
    codigo_apagar = questionary.select("Escolha o cliente para apagar:", clientes_opcoes).ask()

    confirmacao = questionary.confirm("Deseja realmente apagar?").ask()
    if confirmacao == False:
        return

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
        "Voltar"
    ]
    opcao_escolhida = ""

    while opcao_escolhida != "Voltar":
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
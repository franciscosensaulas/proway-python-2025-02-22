import questionary

from src.helpers.tela import limpar_tela
from src.repositorios import pedido_repositorio


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
            "Escolha o menu desejado para o Pedidos:", 
            choices=menu_interno,
        ).ask()
        limpar_tela()
        
        if opcao_escolhida == "Listar todos":
            listar_pedidos()
        elif opcao_escolhida == "Cadastrar":
            cadastrar_pedido()
        elif opcao_escolhida == "Editar":
            editar_pedido()
        elif opcao_escolhida == "Apagar":
            apagar_pedido()


def editar_pedido():
    id_pedido = int(questionary.text("Digite o id do pedido para editar: ").ask().strip())
    quantidade = int(questionary.text("Digite a quantidade: ").ask().strip())
    quantidade_linhas_afetadas = pedido_repositorio.editar(id_pedido, quantidade)
    if quantidade_linhas_afetadas == 1:
        print("Pedido alterado com sucesso")
    else: 
        print("Pedido não encontrado com o id ", id_pedido)


def apagar_pedido():
    id_pedido_apagar = int(questionary.text("Digite o id do pedido para apagar: ").ask().strip())
    linhas_afetadas = pedido_repositorio.apagar(id_pedido_apagar)

    if linhas_afetadas == 1:
        print("Pedido apagado com sucesso")
    else:
        print("Não foi encontrado pedido com este id")


def listar_pedidos():
    pedidos = pedido_repositorio.obter_todos()

    print("Lista de pedidos:")
    for pedido in pedidos:
        print(f"""
Código: {pedido['id']}
Produto: {pedido['produto']}
Quantidade: {pedido['quantidade']}
Preço Unitário: {pedido['preco_unitario']}
Cliente código: {pedido['id_cliente']}
Cliente nome: {pedido['nome_cliente']}""")


def cadastrar_pedido():
    id_cliente = int(questionary.text("Digite o id do cliente para registrar o pedido: ").ask().strip())
    produto = questionary.text("Digite o nome do produto: ").ask().strip()
    quantidade = int(questionary.text("Digite a quantidade: ").ask().strip())
    preco_unitario = float(questionary.text("Digite o preço unitário: ").ask().strip())
    pedido_repositorio.cadastrar(produto, quantidade, preco_unitario, id_cliente)
    print("Pedido cadastrado com sucesso")
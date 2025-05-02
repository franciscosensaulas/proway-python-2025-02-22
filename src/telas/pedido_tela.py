import questionary
from rich.console import Console
from rich.table import Table

from src.helpers.tela import limpar_tela
from src.repositorios import pedido_repositorio


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
    pedidos = pedido_repositorio.obter_todos()
    pedidos_opcoes = [questionary.Choice(pedido.cliente.nome + " - " + pedido.produto, value=pedido.id) 
                       for pedido in pedidos]
    
    id_pedido = questionary.select("Escolha o pedido para editar:", pedidos_opcoes).ask()
    
    pedido_original = pedido_repositorio.obter_por_id(id_pedido) 
    quantidade = int(questionary.text("Digite a quantidade: ", default=str(pedido_original["quantidade"])).ask().strip())
    quantidade_linhas_afetadas = pedido_repositorio.editar(id_pedido, quantidade)
    if quantidade_linhas_afetadas == 1:
        print("Pedido alterado com sucesso")
    else: 
        print("Pedido não encontrado com o id ", id_pedido)


def apagar_pedido():
    pedidos = pedido_repositorio.obter_todos()
    pedidos_opcoes = [questionary.Choice(pedido.cliente.nome + " - " + pedido.produto, value=pedido.id) 
                       for pedido in pedidos]
    
    id_pedido_apagar = questionary.select("Escolha o pedido para apagar:", pedidos_opcoes).ask()

    confirmacao = questionary.confirm("Deseja realmente apagar?").ask()
    if confirmacao == False:
        return

    linhas_afetadas = pedido_repositorio.apagar(id_pedido_apagar)

    if linhas_afetadas == 1:
        print("Pedido apagado com sucesso")
    else:
        print("Não foi encontrado pedido com este id")


def listar_pedidos():
    pedidos = pedido_repositorio.obter_todos()

    print("Lista de pedidos:")
    console = Console()
    tabela = Table()
    tabela.add_column("Código",  style="cyan",)
    tabela.add_column("Cliente",  style="magenta")
    tabela.add_column("Produto", style="green")
    tabela.add_column("Quantidade", style="yellow")
    tabela.add_column("Preço Unitário", style="red")
    tabela.add_column("Total", style="dark_orange")

    for pedido in pedidos:
        tabela.add_row(
            str(pedido.id),
            pedido.cliente.nome,
            pedido.produto,
            str(pedido.quantidade),
            str(pedido.preco_unitario),
            str(pedido.quantidade * pedido.preco_unitario)
        )
    console.print(tabela)


def cadastrar_pedido():
    id_cliente = int(questionary.text("Digite o id do cliente para registrar o pedido: ").ask().strip())
    produto = questionary.text("Digite o nome do produto: ").ask().strip()
    quantidade = int(questionary.text("Digite a quantidade: ").ask().strip())
    preco_unitario = float(questionary.text("Digite o preço unitário: ").ask().strip())
    pedido_repositorio.cadastrar(produto, quantidade, preco_unitario, id_cliente)
    print("Pedido cadastrado com sucesso")
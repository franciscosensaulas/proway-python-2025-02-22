from src.telas import cliente_tela, pedido_tela
from src.helpers.tela import limpar_tela
import questionary

from src.repositorios import pedido_repositorio

if __name__ == "__main__":
    menus = ["Clientes", "Pedidos", "Sair"]
    opcao_escolhida = ""

    limpar_tela()
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select("Escolha o menu desejado:", choices=menus).ask()
        limpar_tela()

        if opcao_escolhida == "Clientes":
            cliente_tela.executar_menu()
        elif opcao_escolhida == "Pedidos":
            pedido_tela.executar_menu()


# No arquivo estrutura.sql criar uma tabela chamada lista_desejos com as seguintes colunas:
#   id inteiro PK
#   produto varchar obrigatório
#   id cliente inteiro FK obrigatório
# Lembrar-se: executar o create table no workbench
# Criar o arquivo lista_desejo_repositorio na pasta repositorios
# Criar os defs: cadastrar, editar, apagar, obter_todos, obter_por_id com pass dentro
# Ex.: def minha_funcao():
#          pass
# Implementar o cadastrar (utilizar como exemplo cadastrar do pedido_repositorio)
# Ir no main.py chamar o cadastrar do lista_desejo_repositorio
# Consultar no banco de dados se deu certo (select ....)

# Implementar o editar (utilizar como exemplo editar do pedido_repositorio)
# Ir no main.py chamar o editar do lista_desejo_repositorio
# Consultar no banco de dados se deu certo (select ....)

# Implementar o apagar (utilizar como exemplo apagar do pedido_repositorio)
# Ir no main.py chamar o apagar do lista_desejo_repositorio
# Consultar no banco de dados se deu certo (select ....)

# Implementar o obter_todos (utilizar como exemplo obter_todos do pedido_repositorio)
# Ir no main.py chamar o obter_todos do lista_desejo_repositorio
# Consultar no banco de dados se deu certo (select ....)
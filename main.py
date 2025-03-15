from src import cliente_db
from src.helpers.tela import limpar_tela
import questionary

if __name__ == "__main__":
    menus = ["Clientes", "Sair"]
    opcao_escolhida = ""

    limpar_tela()
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select("Escolha o menu desejado:", choices=menus).ask()
        limpar_tela()

        if opcao_escolhida == "Clientes":
            cliente_db.executar_menu()

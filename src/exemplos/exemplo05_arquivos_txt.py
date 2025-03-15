import os  # Importa o módulo 'os', que permite interagir com o sistema operacional.

# Define a função que cria o arquivo na área de trabalho
def criar_arquivo_na_area_de_trabalho():
    # Obtém o caminho da área de trabalho do usuário
    caminho_desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # Caminho completo para a área de trabalho
    # Define o nome do arquivo que será criado na área de trabalho
    nome_arquivo = "clientes.txt"
    # Junta o caminho da área de trabalho com o nome do arquivo
    caminho_arquivo = os.path.join(caminho_desktop, nome_arquivo)
    # Pergunta ao usuário para inserir 3 linhas de texto
    linha1 = input("Digite do primeiro cliente: ")
    linha2 = input("Digite do segundo cliente: ")
    linha3 = input("Digite do terceiro cliente: ")
    # Abre o arquivo em modo de escrita ('w'). Se o arquivo não existir, ele será criado.
    with open(caminho_arquivo, 'w') as file:
        # Escreve as linhas no arquivo
        file.write(linha1 + "\n")  # Escreve a primeira linha
        file.write(linha2 + "\n")  # Escreve a segunda linha
        file.write(linha3 + "\n")  # Escreve a terceira linha

    # Exibe uma mensagem para o usuário informando o local onde o arquivo foi salvo
    print(f"O arquivo foi salvo em: {caminho_arquivo}")


# Função para ler o arquivo gerado com while
def ler_arquivo_na_area_de_trabalho():
    # Obtém o caminho da área de trabalho do usuário
    caminho_desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # Caminho completo para a área de trabalho
    # Define o nome do arquivo que será lido
    nome_arquivo = "clientes.txt"
    # Junta o caminho da área de trabalho com o nome do arquivo
    caminho_arquivo = os.path.join(caminho_desktop, nome_arquivo)
    # Verifica se o arquivo existe antes de tentar abrir
    if os.path.exists(caminho_arquivo):
        # Abre o arquivo em modo de leitura ('r')
        with open(caminho_arquivo, 'r') as file:
            # Lê todas as linhas do arquivo
            conteudo = file.readlines()

            # Exibe o conteúdo do arquivo usando while
            print("Conteúdo do arquivo:")
            i = 0  # Inicializa o índice para acessar as linhas
            while i < len(conteudo):  # Enquanto o índice for menor que o número de linhas
                print(conteudo[i].strip())  # Exibe a linha, removendo a quebra de linha
                i += 1  # Incrementa o índice
    else:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")

# Chama a função para criar o arquivo
# criar_arquivo_na_area_de_trabalho()

# Chama a função para ler o arquivo
ler_arquivo_na_area_de_trabalho()

# Exercícios:
# Ex. 1: Solicitar para o usuário o modelo de 4 carros (utilizar while)
#        Armazenar o modelo dos 4 carros no arquivo
# Ex. 2: Ler o arquivo com os nomes dos modelos e apresentar para o usuário
# Ex. 3: Solicatar o preço de um carro para o usuário no seguinte formato: R$ 2.304,50
#        Fazer a limpeza para '2304.50' e converter para float
# Ex. 4: Solicitar o nome e a quantidade de carne para comprar enquanto o usuário digitar 'sim'
#        Usuário pode digitar, sim de qualquer forma: 'SIM', ' sim ', 'Sim '
# Ex. 5: Dado que o usuário digitou o código do cartão de crédito no formato 
#        '2031 2301 4919 2000', extrair a primeira, segunda, terceira e 
#        quanta parte em variáveis. Ex.: primeira parte: 2031
# Ex. 6: Solicitar para o usuário o login e senha, se a senha começar com 12345, 
#        deverá perguntar para o mesmo uma outra senha pois senhas não devem 
#        conter números seguidos. 
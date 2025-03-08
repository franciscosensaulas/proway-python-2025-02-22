import datetime


# Função com 2 parâmetros que retorna uma string
def contenar_dados_jogo(nome_jogo: str, desenvolvedora_jogo: str) -> str:
    texto = nome_jogo + " desenvolvido por "+ desenvolvedora_jogo
    return texto

# Função sem parâmetros que não tem retorno
def mostrar_jogo_detalhes():
    nome = "CS 1.6"
    desenvolvedora = "VALVE"
    texto_apresentar = contenar_dados_jogo(nome, desenvolvedora)
    print(texto_apresentar)

    nome = "The Witcher"
    desenvolvedora = "CD Project Red"
    texto_apresentar = contenar_dados_jogo(nome, desenvolvedora)
    print(texto_apresentar)
   

def somar(n1: int, n2: int) -> int:
    soma: int = n1 + n2
    return soma


def solicitar_numeros_somando() -> int:
    numero1: int = int(input("Digite o número 1: "))
    numero2: int = int(input("Digite o número 2: "))
    # soma: int = numero1 + numero2

    soma = somar(numero1, numero2)
    return soma


def exemplo_calculadora():
    resultado = solicitar_numeros_somando()
    print("Soma: ", resultado)

    resultado = solicitar_numeros_somando()
    print("Soma: ", resultado)


def solicitar_nome() -> str:
    nome: str = input("Digite o nome: ")
    while len(nome) < 3:
        print("Nome deve conter no mínimo 3 caracteres")
        nome: str = input("Digite o nome: ")
    return nome


def solicitar_sobrenome() -> str:
    sobrenome: str = input("Digite o sobrenome: ")
    while len(sobrenome) < 5:
        print("Sobrenome deve conter no mínimo 5 caracteres")
        sobrenome: str = input("Digite o sobrenome: ")
    return sobrenome


def solicitar_idade() -> int:
    idade: int = int(input("Digite a idade: "))
    while idade < 0 or idade > 130:
        print("Idade deve ser entre 0 e 130 anos")
        idade: int = int(input("Digite a idade: "))
    return idade


# Função com 1 parâmetro do tipo int e um retonro do tipo int
def calcular_ano_nascimento(idade: int) -> int:
    data_hora_atual = datetime.datetime.now()
    ano_atual = data_hora_atual.year
    ano_nascimento = ano_atual - idade
    return ano_nascimento

# Função sem retorno, com 4 parâmetros
def apresentar_dados(nome: str, sobrenome: str, idade: int, ano_nascimento):
    import os
    os.system("cls")
    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    print("Idade:", idade)
    print("Ano nascimento:", ano_nascimento)


# Função sem retorno e sem parâmetros
def exemplo_dados_colaborador():
    paciente_nome = solicitar_nome()
    paciente_sobrenome = solicitar_sobrenome()
    paciente_idade = solicitar_idade()

    paciente_ano_nascimento = calcular_ano_nascimento(paciente_idade)

    apresentar_dados(paciente_nome, paciente_sobrenome, paciente_idade, paciente_ano_nascimento)


if __name__ == "__main__":
    exemplo_dados_colaborador()

## Ex.1: Solicitar modelo, ano fabricação, quantidade parcelas, valor mensal, valor fipe
## Calcular o valor do total do carro pago, calcular o total juros
## Validações:
## modelo: min 3 max 20
## ano fabricacao: min 1920 max 2025
## quantidade parcelas: min: 10 max: 60
## valor mensal: min 10.00 max 9999.99

# ## Ex.2: Calculadora de Descontos em Produtos
# Solicite o nome do produto, o preço original e o percentual de desconto.  
# Calcule o valor do desconto e o preço final do produto após o desconto.  
# ### Validações:  
# - **Nome do produto**: mínimo de 3 e máximo de 30 caracteres. `def solicitar_nome`
# - **Preço original**: mínimo de 1.00 e máximo de 10000.00. `def solicitar_preco`
# - **Percentual de desconto**: mínimo de 0.0 e máximo de 100.0. `def solicitar_percentual_desconto`
# Crie funções para:
# 1. Solicitar as entradas (solicitar_nome, solicitar_preco e solicitar_percentual_desconto) do usuário.
# 2. Calcular o valor do desconto a partir do preço original e percentual (calcular_desconto)
# 3. Calcular o preço final após o desconto (calcular_preco_final)
# 4. Apresentar dados (apresentar_dados)

# ## Ex.3: Calculadora de IMC
# Solicite o nome, peso e altura de uma pessoa.  
# Calcule o Índice de Massa Corporal (IMC) e classifique o resultado.  
# A fórmula para o cálculo do IMC é:  
# `IMC = peso / (altura * altura)`  
# ### Validações:  
# - **Nome**: mínimo de 3 e máximo de 30 caracteres.
# - **Peso**: mínimo de 20.0 e máximo de 200.0 kg.
# - **Altura**: mínimo de 1.0 e máximo de 2.5 metros.

# Crie funções para:
# 1. Calcular o IMC.
# 2. Classificar o IMC de acordo com as faixas estabelecidas:
#    - Abaixo de 18.5: Abaixo do peso.
#    - Entre 18.5 e 24.9: Peso normal.
#    - Entre 25.0 e 29.9: Sobrepeso.
#    - Entre 30.0 e 39.9: Obesidade.
#    - Acima de 40.0: Obesidade grave.
# 3. Solicitar as entradas (nome, peso, altura) do usuário e apresentar o IMC e a classificação.


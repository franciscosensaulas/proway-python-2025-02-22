# Variável é o local onde é possível armazenar dado
# O padrão de nomenclatura de variáveis é o snake_case.
# Exemplos de padrões corretos e incorretos
# Não pode começar com número, n pode conter caracter especiais(éçã), 
# n pode ter espaços
# Correto: nome, nome_completo, idade, salario1, cargo, idade_aluno
# Incorreto: Nome, nomeCompleto, Idade, salário, s1, idadealuno

# https://franciscosens.com

def exemplo01_string():
    # criado a variável nome que contém o valor Maria
    nome = "Maria"
    # criado a variável sobrenome que contém o valor Souza
    sobrenome = "Souza"
    # criando a variável nome_completo que conterá o nome completo
    nome_completo = nome + " " + sobrenome
    print("Nome completo:", nome_completo)


def exemplo02_multiplicacao():
    numero1 = 100 # tipo int
    numero2 = 10
    resultado = numero1 * numero2
    print("Resultado da multiplicação:", resultado)


def exemplo03_float():
    # Converter reais para dolar
    valor_em_reais = 250.90 # R$ 250,90 (tipo é o float)
    dolar = 5.70
    valor_convertido = valor_em_reais / dolar
    print("Valor em reais: ", valor_em_reais)
    print("Preço por dolar:", dolar)
    print("Valor em dolares:", valor_convertido)


def exemplo04_boolean():
    # Boolean é utilizado para armazenar valor lógico: true(verdadeiro) ou false(falso)
    nome = "Pedro da Silva"
    esta_matriculado = True 
    # Cancelou a matrícula dele
    esta_matriculado = False

    # se está matriculado for verdadeiro
    if esta_matriculado == True:
        print(nome, "está matriculado:", "sim")
    else: # senão, ou seja, neste cenário n estaria matriculado
        print(nome, "está matriculado:", "não")


def exemplo05_calcular_total_compra():
    # Dados do produto 1 que o usuário quer comprar
    produto1 = "Calça" # string
    quantidade1 = 6 # int
    preco_unitario1 = 130.00 # float

    # Dados do produto 2 que o usuário quer comprar
    produto2 = "Camisa"
    quantidade2 = 5
    preco_unitario2 = 80.30

    # Calcular o total parcial por produto
    total_produto1 = quantidade1 * preco_unitario1
    total_produto2 = quantidade2 * preco_unitario2

    # Calcular o total da compra
    total_parcial = total_produto1 + total_produto2
    
    # Aplicar 10% de desconto
    valor_desconto = total_parcial * 0.10

    # Subtrair do total parcial o valor do desconto
    total = total_parcial - valor_desconto

    print("Produto 1:", total_produto1)
    print("Produto 2:", total_produto2)
    print("Total parcial:", total_parcial)
    print("Desconto:", valor_desconto)
    print("Total:", total)


exemplo05_calcular_total_compra()

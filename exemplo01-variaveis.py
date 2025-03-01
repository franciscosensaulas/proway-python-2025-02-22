    # Variável é o local onde é possível armazenar dados.
    # O padrão de nomenclatura de variáveis é o snake_case.
    # Exemplos de padrões corretos e incorretos.
    # Não pode começar com número, n pode conter caracter especiais


def exemplo01_string():
    # criando a variável nome que contém o valor Maria
    nome = "Maria"
    # criando a variável sobrenome que contém o valor Souza
    sobrenome = "Souza"
    # criando a variável nome_completo que conterá o nome completo
    nome_completo = nome + " " + sobrenome 
    print("nome_completo:", nome_completo)





def exemplo02_multiplicacao():
    numero1 = 100 # tipo int
    numero2 = 10
    resultado = numero1 * numero2
    print("Resultado da multiplicação: ", resultado)





def exemplo03_float():
    # Converter reais para dólar
    valor_em_reais = 250.90 # R$ 250,90 (tipo tipo é o float)
    dolar = 5.70
    valor_convertido = valor_em_reais / dolar
    print("Valor em reais: ", valor_em_reais)
    print("Preço por dolar: ", dolar)
    print("Valor em dolares:", valor_convertido)




def exemplo04_boolean():
    # Boolean é utilizado para armazenar valor lógico: true(verdadeiro) ou false(falso)
    nome = "Pedro da Silva"
    esta_matriculado = True
    # Cancelou a matricula dele
    esta_matriculado = False

    # se está matriculado for verdadeiro
    if esta_matriculado == True:
        print(nome, "está matriculado:", "sim")
    else: # senão, ou seja, neste cenário não estaria matriculado
        print(nome, "está matriculado:", "não")


def exemplo05_calcular_total_compra():
    # Dados do produto 1 que o usuário quer comprar
    produto1 = "Calça" # String
    quantidade1 = 6 # int 
    preco_unitario1 = 130.00 # float

    # Dados do produto 2 que o usuário quer comprar
    produto2 = "Camisa"
    quantidade2 = 5
    preco_unitario2 = 80.30

    # Calcular o total parcial por produto
    total_produto1 = quantidade1 * preco_unitario1
    total_produto2 = quantidade2 * preco_unitario2

    # calcular o total da compra
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



def exercicio01_apresentar_cliente():
    # criar as seguintes variáveis nome, idade, cpf, apresentar todos os dados do cliente, alterar a idade do cliente e criar a variável endereço.
    nome = "Jeferson"
    idade = 32
    cpf = "08275280940"
    endereco = "Rua George Fridrich Mordshorst, 663"
    print(nome)
    print(idade, "Anos")
    print(cpf)
    print(endereco)


def exercicio03_calcular_ano_nascimento():
    # criar uma variável para armazenar a idade de uma pessoa, outra para armazenar o ano atual, e por último              calcule e mostre o ano de nascimento da pessoa.
    idade = 32
    ano_atual = 2025
    nascimento = ano_atual - idade
    print(nascimento)


def exercicio04_mostrar_saldo_bancario():
    # crie variáveis para armazenar o nome de um cliente e o saldo da conta.
    # Mostre o nome do cliente e o saldo da conta.
    # Tire 20 reais da conta
    # Mostre o nome do cliente e o saldo na conta.
    # Adicione 75.20 reais no saldo da conta.
    # Mostre o nome do cliente e o saldo da conta.
    nome = "Jeferson"
    saldo_da_conta = 256.00
    print(nome)
    print(saldo_da_conta)
    saldo_atual = saldo_da_conta - 20
    print(nome)
    print(saldo_atual)
    saldo_atual = saldo_atual + 75.20
    print(nome)
    print("esse é seu saldo atualizado prezado cliente", saldo_atual)

exercicio04_mostrar_saldo_bancario()








    








    






    








 





    













    

    







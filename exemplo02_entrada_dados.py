def solicitar_nome_completo():
    # print("Digite o seu nome:", end="")

    # input permite o usuário digitar
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")

    # Armazenando na variável nome_completo a concatenação do nome, espaço e sobrenome
    nome_completo = nome + " " + sobrenome

    # Apresentar para o usuário o nome completo
    print("Nome Completo:", nome_completo)


def solicitar_dados_paciente():
    # input é utilizado para solicitar dado para o usuário
    # tudo que o input digita vem como texto
    # int(input("Digite a idade")) => solicita para o usuário a idade que vem como 
    # string(texto) e é convertida para int(inteiro) 

    paciente = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    peso = float(input("Digite o peso do paciente: "))
    altura = float(input("Digite a altura do paciente: "))

    # Calcular o IMC do paciente: peso / altura²
    imc = peso / (altura * altura)

    print("O paciente", paciente, "tem o IMC de", imc)

    # if: se
    # else: senão
    # elif: else if => senão se

    if imc < 18.5: # se o imc é menor que 18.5
        print("IMC: Abaixo do peso")
    elif imc <= 24.99: # senão se o imc é menor que 25, elif => else if
        print("IMC: Normal")
    # Apresentar o restante da tabela

# Criar um def chamado solicitar_dados_curso
# Solicitar o nome do curso, quantidade de horas, valor parcela, quantidade parcelas
# Calcular o valor total do curso
# Se o valor do curso for menor que 100 reais, apresentar que o curso é gratuito
# Se o valor do curso for maior ou igual a 100 reais, apresentar o valor total do curso

# Criar um def chamado solicitar_notas_aluno
# Solicitar nome do aluno, nota 1, nota 2 e nota 3
# Calcular a média
# Apresentar a média
# Apresentar o status da média:
# - Se a média for entre 7 e 10, aluno aprovado
# - Se a média for entre 0 e 4.99, aluno reprovado
# - Se a média for entre 5 e 6.99, aluno em exame

# Tabela verdade E(and)
# V e V => V
# V e F => F
# F e V => F
# F e F => F



def solicitar_idade():
    idade = int(input("Digite a idade"))
    # entre 11 e 17
    if idade >= 11 and idade <= 17:
        print("Adolescente")
    elif idade >= 18 and idade <= 64:
        print("Adulto")
    elif idade >= 65:
        print("Idoso")
    else:
        print("Criança")
    print("Fim")


def solicitar_pacote_viagem():
    # string em linha, porém contém quebras de linha
    # pacote_viagem = input("1 - Pacote Disney\n2 - Pacote Chile\n3 - Pacote Londres\n4 - Fernando de Noronha")

    # string em multilinhas
    pacote_viagem = int(input("""Pacotes de viagem:
1 - Pacote Disney
2 - Pacote Chile
3 - Pacote Londres
4 - Fernando de Noronha
Escolha o número do pacote de viagem: """))
    
    # Operador Lógico OR(ou)
    # Tabela verdade do Ou
    # V ou V => V
    # V ou F => V
    # F ou V => V
    # F ou F => F

    if pacote_viagem == 1 or pacote_viagem == 3:
        print("Passaporte é necessário")
    elif pacote_viagem == 2 or pacote_viagem == 4:
        print("Sem passaporte")
    
    if pacote_viagem == 1:
        preco_viagem = 20_000.12
    elif pacote_viagem == 2:
        preco_viagem = 8_000.00
    elif pacote_viagem == 3:
        preco_viagem = 25_000.00
    elif pacote_viagem == 4:
        preco_viagem = 12_000_00
    else:
        print("Pacote de viagem não existe")
        return

    quantidade_vezes = 1
    
    # se o preço da viagem for maior que R$18.000,00 permitiremos parcelar a viagem
    if preco_viagem > 18_000.00:
        quantidade_vezes = int(input("Digite a quantidade de parcelas para o pagamento: "))
    
    
    preco_parcela = preco_viagem / quantidade_vezes
    print("A quantidade de parcelas é: ", quantidade_vezes)
    print("O valor da parcela é: ", quantidade_vezes)
    print("Total: ", preco_viagem)



if __name__ == "__main__":
    solicitar_pacote_viagem()
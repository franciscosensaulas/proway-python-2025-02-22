def solicitar_nome_completo():
    print("Digite o seu nome:", end="")

    # input permite o usuário digitar
    nome = input("Digite o seu nome:")
    sobrenome = input("Digite o seu sobrenome: ")

    # nome_completo a concatenação do nome, espaço e sobrenome
    nome_completo = nome + " " + sobrenome

    # Apresentar para o usuário o nome completo
    print("Nome Completo:", nome_completo)


def solicitar_dados_paciente():

    # input é utilizado para solicitar dado para o usuário
    # tudo que o input digita vem como texto
    # int(input("Digite a idade"))=> solicita para o usuário a idade que vem como
    # string (texto) e é convertida para int(inteiro)

    paciente = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    peso = float(input("Digite o peso do paciente: "))
    altura = float(input("Digite a altura do paciente: "))

    # calcular o IMC do paciente: peso / altura²
    imc = peso / (altura * altura)

    print("O paciente", paciente, "tem o IMC de", imc)

    if imc < 18.5: # se o imc é menor que 18.5
        print("IMC: Abaixa do peso")
    elif imc <= 24.99: # senão se o imc é menor que 25, elif => else if
        print("IMC: normal")
    elif imc <= 29.99: 
        print("IMC: Excesso de peso")   
    elif imc <= 34.99:
        print("IMC Obesidade classe 1")
    elif imc <= 39.99:
        print("Obesidade classe 2")
    elif imc >= 40:
        print("Obesidade classe 3")


def solicitar_dados_curso():

    nome_curso = input("Qual o curso que você está fazendo:")
    quantidade_horas = int(input("Qual a carga horária do curso:"))
    valor_total_curso = input("Quanto você irá pagar por este curso:")
    quantidade_parcelas = input("Em quantas parcelas você dividiu o valor do curso:")
    valor_mensal = 500

    valor_total = valor_mensal * quantidade_parcelas
    if  valor_total_curso < 100:
        print("O curso será Gratuito")
    elif valor_total_curso > 100:
        print("O valor total desse curso é:", valor_total_curso) 



def solicitar_notas_aluno():
    nome = input("Qual é o seu nome:")
    nota1 = float(input("Informe a primeira nota:"))
    nota2 = float(input("Informe a segunda nota:"))
    nota3 = float(input("Informe a terceira nota:"))
    soma_notas = (nota1 + nota2 + nota3) / 3
    print("essa foi sua média:", soma_notas)
    # apresentar o status da média
    if soma_notas >= 7 and soma_notas <= 10:
        print("Aluno aprovado")
    elif soma_notas >= 0 and soma_notas <= 4.99:
        print("Aluno reprovado")
    else:
        print("Aluno em exame de recuperação")


def solicitar_pacote_viagem():
    # string em linha, porém contém quebras de linha.
    # pacote_viagem = input("1 - pacote Disney\n2 - Pacote Chile\n3 - Pacote Londres\n4 - Fernando Noronha")

    # string em multilinhas
    pacote_viagem = int(input("""Pacotes de viagem:
1 - Pacote Disney
2 - Pacote Chile
3 - Pacote Londres
4 - Fernando de Noronha
Escolha o número do pacote de viagem: """))
    # Operador logico OR(ou)
    # Tabela verdade do OU
    # V ou V => V
    # V ou F => V
    # F ou V >= V
    # F ou F >= F

    if pacote_viagem == 1 or pacote_viagem == 3:
        print("Passaport é necessário")
    elif pacote_viagem == 2 or pacote_viagem == 4:
        print("Sem passaporte")

    if pacote_viagem == 1:
        preco_viagem = 20_000.00
    elif pacote_viagem == 2:
        preco_viagem = 8_000.00
    elif pacote_viagem == 3:
        preco_viagem = 25_000.00
    elif pacote_viagem == 4:
            preco_viagem = 12_000.00
    else:
        print("Pacote de viagem não existe")
        return

    # se o preço da viagem for maior que R$18.000,00 permitiremos parcelar a viagem
    if preco_viagem > 18_000.00:
        quantidade_vezes = int(input("Digite a quantidade de parcelas para o pagamento: "))
    else:
        quantidade_vezes = 1

    preco_parcela = preco_viagem / quantidade_vezes
    print("A quantidade de parcelas é: ", quantidade_vezes)
    print("O valor é : ", quantidade_vezes)
    print("Total: ", preco_viagem)


def verificar_acesso():
    idade = int(input("Qual a sua idade"))
    estudante = input("Você é um estudante ")
    if idade < 18 or estudante == "sim":
        print("Acesso será permitido com desconto")
    else:
        print("Acesso liberado sem desconto, será necessário pagar o valor cheio de ingresso")


def avaliar_risco_investimento():
    
    investimentos_disponiveis = int(input(""" investimentos_disponiveis:
   1 - investimentoA
   2 - investimentoB
   3 - investimentoC
   Escolha qual investimento deseja: """ ))
    if investimentos_disponiveis == 1 or investimentos_disponiveis == 2:
        print("Esse investimento é de risco Alto")
    else : 
        print("Esse investimento é de baixo Risco")


def verificar_eligibilidade ():
    idade = int(input("Informe a sua idade "))
    media = float(input("Digite a sua média "))
    if idade < 25 or media >= 8:
        print("Você está elegível para ganhar a bolsa")
    else:
        print("Infelizmente você não atendeu os requisitos")







    


    




    
    





    


if __name__ == "__main__":
    verificar_eligibilidade ()
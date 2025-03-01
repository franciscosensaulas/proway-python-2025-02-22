import os


def exemplo_apresentar_contagem():
    indice = 0 
    # enquanto indice for menor 10, faça
    while indice <= 10:
        print(indice)

        indice = indice + 1
    print("Finalizado contagem de 0 até 10")

# 0..10 indice < 11, indice <= 10

def exemplo_solicitar_numeros():
    indice = 0
    # solicitar 5 números
    while indice < 5:
        numero = int(input("Digite o número: "))

        # incrementar
        indice = indice + 1
    
def exemplo_media_notas():
    indice = 0
    # Solicitar o nome e 3 notas do aluno
    nome_aluno = input("Digite o nome do aluno: ")
    
    soma_notas = 0
    while indice < 3:
        nota = float(input("Digite a nota do aluno: "))

        soma_notas = soma_notas + nota
        indice = indice + 1
    media = soma_notas / 3
    print("Média", media)


def exemplo_notas_varios_alunos():
    indice = 0
    while indice < 2:
        nome_aluno = input("Digite o nome do aluno: ")
        indice_notas = 0
        while indice_notas < 3:
            nota = float(input("Digite a nota do aluno: "))
            indice_notas = indice_notas + 1
        indice = indice + 1


def exemplo_descobrir_maior_salario():
    quantidade_colaboradores = 4
    indice = 0
    maior_salario = 0
    while indice < quantidade_colaboradores:
        nome = input("Digite o nome do colaborador: ")
        salario = float(input("Digite o salário: "))
        print("\n\n")

        if salario > maior_salario:
            maior_salario = salario

        # incrementar
        indice = indice + 1
    print("Maior salário:", maior_salario)


def exemplo_descobrir_menor_salario():
    menor_salario = 1_000_000_000
    quantidade_desejada = int(input("Digite a quantidade desejada para cadastrar: "))
    indice = 0
    while indice < quantidade_desejada:
        salario = int(input("Digite o salário: "))
        if salario < menor_salario:
            menor_salario = salario
        indice = indice + 1
    print("Menor salário:", menor_salario) 


def exemplo_executar_enquanto_desejar():
    confirmacao = input("Deseja calcular a média? [s/n]: ")
    while(confirmacao != "n"):
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        nota3 = float(input("Digite a nota 3: "))
        media = (nota1 + nota2 + nota3) / 3

        print("Média: ", media)

        confirmacao = input("Deseja calcular a média? [s/n]: ")
        
        # limpar o console
        os.system("cls")


def quantidade_habitantes_de_blumenau():
    quantidade_pessoas_pesquisa = 5
    indice, quantidade_blumenau, quantidade_outras = 0, 0, 0
    while indice < quantidade_pessoas_pesquisa:
        nome_cidade = input("Digite o nome da cidade: ")
        if nome_cidade.lower().strip() == "blumenau":
            quantidade_blumenau = quantidade_blumenau + 1
        else:
            quantidade_outras = quantidade_outras + 1
        indice = indice + 1
    print("Habitantes de Blumenau:", quantidade_blumenau)
    print("Habitantes de outras cidades:", quantidade_outras)


if __name__ == "__main__":
    quantidade_habitantes_de_blumenau()

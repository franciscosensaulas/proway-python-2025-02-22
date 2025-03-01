def remover_espacos_comeco():
    texto = "   Meu texto   "

    print("Texto original: '", texto, "'terminou texto")

    text_sem_espacos_comeco = texto.lstrip()
    print("Texto removido espaços do começo: '", text_sem_espacos_comeco, "' terminou texto", sep="")


def remover_espacos_final():
    texto = "   Meu texto   "
    print("Texto original: '", texto, "' terminou texto", sep="")
    texto_sem_espacos_final = texto.strip() # remover os espaços da direita
    print("Texto removido espaços do começo e do final:'", texto_sem_espacos_final, "' terminou texto", sep="")


def converter_letra_minuscula():
    opcao = "SIM"

    opcao_sanitizada = opcao.lower() # ' sim '
    if opcao_sanitizada == "sim":
        print("Usuário aceitou")
    else:
        print("Usuárionão aceitou")


def converter_letra_maiuscula():
    nome_completo = "Jeferson Pereira de Almeida"

    nome_completo_sanitizada = nome_completo.upper() # Trazer o nome em Letra Maiuscula
    print("Nome completo: ", nome_completo_sanitizada)


def quantidade_pessoas_comecam_enzo():
    indice = 0
    quantidade_enzo = 0
    while indice < 4:
        nome_completo = input("Digite o nome completo: ")
        if nome_completo.startswith("Enzo"):
            quantidade_enzo = quantidade_enzo + 1
        indice = indice + 1
    print("Quantidade de enzos(s): ", quantidade_enzo)


def quantidade_empresas_ltda_que_terminam_com_ltda():
    indice = 0
    quantidade_ltda = 0
    while indice <4:
        empresa = input("Digite o nome da empresa: ")
        # endswith = terminar com exemplo.....
        if empresa.upper().endswith("LTDA"):
            quantidade_ltda = quantidade_ltda + 1
        indice = indice + 1
    print("Quantidade de empresas LTDA: ", quantidade_ltda)


def obter_quantidade_caracteres_string():
    texto = "Um texto ai "
    # len => length que é utilizado para saber o comprimento de uma string 
    quantidade_caracteres = len(texto)
    print("Texto: '", texto, "'", sep="")
    print("Quantidade de caracteres:", quantidade_caracteres)


def substituir_caracteres_na_string():
    cpf_formatado = "082.752.809-40"
    cpf = cpf_formatado.replace(".", "").replace("-", "")
    print("CPF formatado:", cpf_formatado)
    print("CPF sem formatação:", cpf)


def extrair_partes_da_string():
    # primeira barra está na posiçao 2
    # o número 7 está na posição 9
    #                  0123456789
    data_nascimento = "12/12/2007"
    dia = data_nascimento[0:2]
    mes = int(data_nascimento[3:5])
    ano = data_nascimento[6:10]
    print("Dia:", dia)
    print("Mês:", ano)
    print("Ano:", ano)

    if mes == 1:
        mes_extenso = "Janeiro"
    elif mes == 2:
        mes_extenso = "Fevereiro"
    elif mes == 3:
        mes_extenso = "Março"
    elif mes == 4:
        mes_extenso = "Abril"
    elif mes == 5:
        mes_extenso = "Maio"
    elif mes == 6:
        mes_extenso = "Junho"
    elif mes == 7:
        mes_extenso = "Julho"
    elif mes == 8:
        mes_extenso = "Agosto"
    elif mes == 9:
        mes_extenso = "Setembro"
    elif mes == 10:
        mes_extenso = "Outubro"
    elif mes == 11:
        mes_extenso = "Novembro"
    elif mes == 12:
        mes_extenso = "Dezembro"

    print("Enzo nasceu no dia: ", dia, " de ", mes_extenso, " de ", ano, ".", sep="")



def extrair_partes_por_delimitador():
    data_nascimento = "18/09/1992"
    dia, mes, ano = data_nascimento.split("/")
    print(dia)
    print(mes)
    print(ano)

def extrair_partes_do_email():
    email_completo = "Franciscosens@proway.com"
    user_name, dominio_completo = email_completo.split("@")
    dominio, _ = dominio_completo.split(".")
    print(user_name)
    print(dominio)


def extrair_data_hora_por_delimitador():
    data_hora_nascimento = "21/03/2014 23:40:59"
    data_nascimento, hora_nascimento = data_hora_nascimento.split(" ")

    hora, minuto, segundo = hora_nascimento.split(":")
    dia, mes, ano = data_nascimento.split("/")

    print("Dia:", dia)
    print("Mes:", mes)
    print("Ano:", ano)
    print("Hora:", hora)
    print("Minuto:", minuto)
    print("Segundo:", segundo)




if __name__ == "__main__":
    extrair_data_hora_por_delimitador()





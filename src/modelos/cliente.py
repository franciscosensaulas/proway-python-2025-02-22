from typing import List


class Cliente:
    # atributos são características que uma classe tem
    id: int
    nome: str
    cpf: str

    # Construtor: é um método que é chamado na instancia do obejto
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.cpf = ""


def exemplo_instancia_objeto():
    # instanciando um objeto da classe Cliente
    joao = Cliente()  # nome_objeto = NomeClasseQueEstamosInstanciando()
    # definindo valor para os atributos
    joao.id = 1
    joao.nome = "João da Silva"
    joao.cpf = "120.291.399-28"

    # alterando o atributo nome do objeto joao
    joao.nome = "João da Silva Souza"

    # apresentar os atributos do objeto (joao) da classe Cliente
    print("\n\nId:", joao.id)
    print("Nome:", joao.nome)
    print("CPF:", joao.cpf)


def exemplo_instancia_objeto_armazenando_lista():
    maria = Cliente()
    maria.nome =  "Maria"

    rubens = Cliente()
    rubens.nome =  "Rubens"

    clientes : List[Cliente] = []
    clientes.append(maria) # posição 0
    clientes.append(rubens)

    for cliente in clientes:
        print(cliente.nome)

from src.modelos.cliente import Cliente


class Pedido:
    id: int
    produto: str
    quantidade: int
    preco_unitario: float

    cliente: Cliente

    def __init__(self):
        self.id = 0
        self.produto = ""
        self.quantidade = 0
        self.preco_unitario = 0.0

        self.cliente = Cliente()
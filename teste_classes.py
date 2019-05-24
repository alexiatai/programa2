class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Item(Produto):
    def __init__(self, produto, quantidade):
        self.produto = Produto(nome, preco)
        self.quantidade = quantidade


class Cestinha():
    def __init__(self, itens):
        self.itens = itens

class Caixa():
    def __init__(self, data, hora, produto, itens):
        self.data = data
        self.hora = hora
        self.produto = produto
        self.itens = itens

    def calcular_preco(self, preco ,quantidade):
        preco_prod = preco*quantidade
        self.itens.append(preco_prod)
        return preco_prod

    def calcular_total(self, itens):
        valor_total = sum(self.itens)
        return valor_total

        

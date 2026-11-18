class Livro:
    total_titulos = 0
    def __init__(self,titulo,autor,qtde,preco=19.99):
        self.__titulo = titulo
        self.autor = autor
        self.__qtde = qtde
        self.preco = preco
        Livro.total_titulos += 1

    def __str__(self):
        return f"{self.titulo} - Autor: {self.autor}"

    def __eq__(self, book):
        return self.titulo == book.titulo

    def __lt__(self, preco_medio):
        return self.preco < preco_medio

    def __len__(self):
        return len(self.titulo)
    
    # Getters
    @property
    def titulo(self):
        return self.__titulo

    @property
    def qtde(self):
        return self.__qtde

    # Setters
    @titulo.setter
    def titulo(self,novo_titulo):
        self.__titulo = novo_titulo

    @qtde.setter
    def qtde(self, nova_qtde):
        if nova_qtde < 0:
            raise ValueError("Stock não pode ser negativo")
        self.__qtde = nova_qtde

    def valor_stock(self):
        return self.__qtde * self.preco

    def atualizar_stock(self, qtde_vendida):
        if qtde_vendida > self.__qtde:
            print(f"Stock ({self.__qtde} unidades) insuficiente!")
        else:
            self.__qtde -= qtde_vendida

    def json(self):
        return { "id": self.id, "titulo": self.__titulo, "autor": self.autor, "qtde": self.__qtde, "preco": self.preco }

    @classmethod
    def atualizar_total_livros(cls, total_livros_qtde_zero):
        return cls.total_titulos - total_livros_qtde_zero

    @classmethod
    def criar_livro(cls, dados):
        return cls(dados["titulo"],dados["autor"],dados["qtde"],dados["preco"])

    # Este método permite verificar se o preço de um livro é válido. 
    # Não necessita de aceder aos atributos da instância nem aos atributos da classe.
    @staticmethod
    def validar_preco(preco):
        if preco > 0:
            return True
        return False
        
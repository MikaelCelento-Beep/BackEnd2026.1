class Produto:
    def __init__(self, nome_produto, preco_produto):
        self.produto = nome_produto
        self.preco = preco_produto

    def produto_info(self):
        print(f"O {self.produto} custa {self.preco}R$")

class Livro:
    def __init__(self, nome_livro, categoria_livro):
        self.livro = nome_livro
        self.categoria = categoria_livro

    def livro_info(self):
        mensagem = (f"O livro se chama {self.livro} e sua categoria é {self.categoria}")
        return mensagem

class Filme:
    def __init__(self, nome_filme, categoria_filme):
        self.filme = nome_filme
        self.categoriafilme = categoria_filme

    def filme_info(self):
        print(f"O filme que vou assistir é {self.filme} e a categoria dele é {self.categoriafilme}")


produto = Produto("Biscoito", "7")
livro = Livro("Komi não consegue se comunicar", "Romance")
filme = Filme("Doutor Estranho no multiverso da loucura", "Ação")

produto.produto_info()

print(30*"=")

print(livro.livro_info())

print(30*"=")

filme.filme_info()
#Sistema Biblioteca

#Define as listas
livros = []
emprestados = []
pedir = []

#Função de mensagem 
def mensagem(msg):
    print(msg)

#Função cadastrar livro
def cadastrar_livros(livro,emprestado):
    #append adiciona itens na lista
    livros.append(livro)
    emprestados.append(emprestado)

#Mostra os livros cadastrados
def livros_disponiveis():
    #len identifica posição dos itens na lista
    for i in range (len(livros)):
        mensagem(f"{i} - {livros[i]} - x{emprestados[i]}")

#Permite que o usúario pegue os livros cadastrados
def pedir_livros(pedido):
    pedir.append(emprestados[pedido])

#Mostra a quantidade de livros que o usúario pegou emprestado
def quantidade_de_livros():
    return sum(pedir)

#Menu de opções para o usúario
def biblioteca():
    print("\n==== Biblioteca do Python ====")
    print("1 - Cadastrar Livros\n2 - Mostrar livros disponíveis\n3 - Fazer emprestimo\n4 - Total de emprestimos realizados\n5 - Sair")


#Parte da programação
def main():
    while True:
        biblioteca()
        opcao = int(input("Escolha a ação a ser realizada pelo número: "))
        if opcao == 1:
            livro = input("Nome do livro: ")
            emprestado = int(input("Informe a quantidade de livros: "))
            cadastrar_livros(livro, emprestado)
            mensagem("Livro cadastrado com sucesso!")

        elif opcao == 2:
            mensagem("\n=== Livros disponíveis ===")
            livros_disponiveis()

        elif opcao == 3:
            mensagem("\n=== Livros disponíveis ===")
            livros_disponiveis()
            escolha = int(input("Escolha o livro pelo número: "))
            pedir_livros(escolha)
            mensagem("Empréstimo realizado com sucesso!")

        elif opcao == 4:
            mensagem(f"O total de livros emprestados é {quantidade_de_livros()}")
        elif opcao == 5:
            mensagem("Encerrando...")
            break
        else: 
            mensagem("Opcão Inválida!")
main()
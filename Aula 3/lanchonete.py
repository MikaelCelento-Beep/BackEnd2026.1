#Sistema lanchonete

#Define as listas
lanches = []
precos = []
pedidos = []


#Função de mensagem 
def mensagem(msg):
    print(msg)

#Função cadastrar lanche
def cadastrar_lanche(lanche, preco):
    #append adiciona itens na lista
    lanches.append(lanche)
    precos.append(preco)

def cardapio():
    #len identifica posição dos itens na lista
    for i in range (len(lanches)):
        mensagem(f"{i} - {lanches[i]} - R${precos[i]}")

def fazer_pedido(pedido):
    pedidos.append(precos[pedido])

def calcular_total():
    return sum(pedidos)

def menu():
    print("\n==== Lanchonete ====")
    print("1 - Cadastrar Lanche\n2 - Mostrar Cardápio\n3 - Fazer Pedido\n4 - Mostrar total/\n5 - Sair")


#Aqui acontece a mágica(Programação(Função Main))
def main():
    while True:
        menu()
        opcao = int(input("Escolha sua opção pelo número: "))
        if opcao == 1:
            lanche = input("Nome do lanche: ")
            preco = float(input("Informe o preço R$"))
            cadastrar_lanche(lanche, preco)
            mensagem("Lanche cadastrado com sucesso!")
        elif opcao == 2:
            mensagem("\n==== Cardápio ====")
            cardapio()
        elif opcao == 3:
            mensagem("\n==== Cardápio ====")
            cardapio()
            escolha = int(input("Escolha o lanche pelo número: "))
            fazer_pedido(escolha)
            mensagem("Pedido realizado!")
        elif opcao == 4:
            mensagem(f"O total é R${calcular_total()}")
        elif opcao == 5:
            mensagem("Saindo...")
            break
        else: 
            mensagem("Opcão Inválida!")
main()


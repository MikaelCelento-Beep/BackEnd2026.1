class Jogos:
    def __init__(self,nome_jogo,categoria_jogo,preco_jogo):
        self.nome = nome_jogo
        self.categoria = categoria_jogo
        self.preco = preco_jogo
        
    def mostrar_dados(self):
        print(f'O {self.nome},\né da categoria {self.categoria},\npreço: R${self.preco}')


#-------------------------------------------------------------------------
class Loja:
    def __init__(self):
        self.jogos = [] #Lista que guarda os jogos

    def cadastar_jogo(self):
        namegame = input("Digite o nome do jogo: ")
        categorygame = input("Digite a categoria do jogo: ")
        pricegame = int(input("Qual o valor do jogo: "))       

        #Instancia a clase Jogos dentro da classe Loja
        #Herança é uma ligação (Loja ao Jogos)
        meus_jogos = Jogos(namegame,categorygame,pricegame) #Objeto - Caacterisiticas

        self.jogos.append(meus_jogos)#Cadastra o objeto na lista
        print("Jogo Cadastrado!\n")
    
    def mostrar_jogos(self):
        print('\n==== JOGOS CADASTRADOS ====')        
        for meus_jogos in self.jogos:
            meus_jogos.mostrar_dados()

    def main(self): 
        while True:
            try:
                opcao = int(input("\nEscolha um opção:\n[1 - cadastrar]\n[2 - Mostrar]\n[3 - Sair]\n ->"))
                if opcao == 1:             
                    self.cadastar_jogo()
                elif opcao == 2:
                    self.mostrar_jogos()
                elif opcao == 3:
                    print("\nEncerrando sessão...")
                    break
            except ValueError:
                print(46*("-"))
                print("Opção inválida! Por favor, tente novamente.")


print(46*("-"))

jg = Loja()
jg.main()
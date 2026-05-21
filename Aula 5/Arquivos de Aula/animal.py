class Animal:
    #Metodo construtor (Inicialização)
    def __init__(self, nome_animal, idade_animal, raca_animal, tipo_animal, som_animal):    
        #self.nome - cria um espaço na memoria
        self.nome = nome_animal
        self.idade = idade_animal
        self.raca = raca_animal
        self.tipo = tipo_animal
        self.som = som_animal

    def desc_animal(self):
        print(f"O {self.tipo} se chama {self.nome} e possui {self.idade}. Sua raça é {self.raca}")

    def emitir_som(self):
        mensagem = (f"O {self.tipo} chamado {self.nome} faz {self.som}")
        return mensagem
    
cachorro = Animal("Amora", "2 meses", "Shitzu", "Cachorro", "Au Au" )
cachorro.desc_animal()
print(cachorro.emitir_som())

print(40*"=")

gato = Animal("Fifi", "2 anos", "Vira-lata", "Gato", "Miau")
gato.desc_animal()
print(gato.emitir_som())
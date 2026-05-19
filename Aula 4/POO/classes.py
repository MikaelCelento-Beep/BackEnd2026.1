#A palavra class é a palavra reservada para criar uma classe
#A classe é um molde do objeto
#Iniciar o nome da classe com letra maíscula
class Carro:

    #Metodo = função
    #self representa o proprio metodo e seus elementos
    def buzinar(self):
        print("Bibibi")
    def andar(self):
        print("Em movimento")



#Cria o objeto utilizando a class(Molde)
carro_um = Carro() #Instanciar a classe
carro_um.buzinar()
carro_um.andar()

class Pessoa:

    def falar(self):
        print("Olá, tudo bem ?")
    def mastigar(self):
        print("Nhac Nhac")



mikael = Pessoa() #Quando instância criamos um objeto
mikael.falar()
mikael.mastigar()

junior = Pessoa()
junior.falar()
junior.mastigar()


class Animal:
    def latir(self):
        print("Wof wof")

class Computador:
    def teclar(self):
        print("tec tec tec")

class Celular:
    def foto(self):
        print("tick tick")

cachorro = Animal()
cachorro.latir()

pc = Computador()
pc.teclar()

telefone = Celular()
telefone.foto()

class Aluno:

    #Método construtor(Tudo que tiver sera criado automaticamente quando a classe for usada)
    #O método __init__ é um método padrão
    def __init__(self, nome_aluno, idade_aluno):

        #Atributos - variaveis metidas
        self.nome = nome_aluno
        self.idade = idade_aluno

    def estudar(self):
        print(f"{self.nome}, está cursando python")



aluno_um = Aluno("Mikael", 17)

print(f"Nome: {aluno_um.nome}")
print(f"Idade: {aluno_um.idade}")
aluno_um.estudar()

print(20*"-")

aluno_dois = Aluno("Pedro", 16)

print(f"Nome: {aluno_dois.nome}")
print(f"Idade: {aluno_dois.idade}")
aluno_dois.estudar()

print(20*"-") 

nome = input("Informe o nome do primeiro aluno: ")
idade = int(input("Informe a idade do aluno: "))

aluno_tres = Aluno(nome, idade)
print(f"O nome do aluno é: {aluno_tres.nome}")
print(f"E sua idade é: {aluno_tres.idade}")
aluno_tres.estudar()
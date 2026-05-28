from django.shortcuts import render

#Importar a classe (Ferramenta) HttpResponse
from django.http import HttpResponse #Vai responder a solicitação do navegador

def ola_mundo(request):
    return HttpResponse("<h1>Olá Mundo!</h1>" "<p>Ola Django!<p>")

def contato(request):
    return HttpResponse("<h1>Contato</h1>  <form>  <input type=text placeholder=email@email.com>  <input text=text placeholder=(21)99999-9999> <button>enviar</button> </form>")


#Chamar ARQUIVOS HTML (Template)
def home(request):
    #Conceito de context (contexto)
    #Context - Pega dados na view e passa para o template

    titulo = "Nossos clientes"
    nosso_cliente = {
        'nome':"Mikael Celento Esperança",
        'idade':17,
        'nascimento': "19/07/2008"
    }

    nomes_clientes = ["Maria", "Joao", "Matheus", "Ana", "Marcos"]

    carros = [
        {'marca': "Chevrolet", 'modelo': "Onix LT", 'ano': "2020"},
        {'marca': "Fiat", 'modelo': "Uno", 'ano': "2010"}
    ]

    return render(request, "clientes/home.html", {'mensagem':titulo, 'lista_cliente':nosso_cliente, 'dados':nomes_clientes, 'meus_carros':carros})

def contact(request):
    return render(request, "contatos/cont.html")
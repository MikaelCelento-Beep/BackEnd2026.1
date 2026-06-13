from django.shortcuts import render

# Create your views here.

""" 
Criar uma pagina onde ele consiga visualizar os clientes cadastrados em formato de tabela

Vsualizar: 
Nome, Idade, Data_Nascimento

Dados devem vir de uma lista de dicionario
"""
def home(request):
    titulo = "Pagina Inicial"
    return render(request, 'clientes/home.html', {'titulo': titulo})

def dados_clientes(request):
    titulo = "Nossos Clientes"
    nossos_clientes = [
        {'nome': "Son Gohan", 'idade': ' 26 anos', 'nascimento': '18/05/2000'},
        {'nome': "Pedro Henrique", 'idade': '29 anos', 'nascimento': '22/03/1997'},
        {"nome": "Julia Barbosa", "idade": '35 anos', "nascimento": "27/07/1988"}
    ]
    return render(request, 'clientes/dados_clientes.html', {'titulo': titulo, 'dados_clientes':nossos_clientes})

def formulario(request):
    titulo = "Cadastro Clientes"
    return render(request, 'clientes/form.html', {'titulo':titulo})
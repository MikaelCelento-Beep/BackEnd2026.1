from django.shortcuts import render

# Create your views here.

def home(request):
    titulo = "Página Inicial"
    return render(request, 'cliente/home.html', {'titulo': titulo})

def dados_clientes(request): 
    titulo = "Nossos Clientes"
    nossos_clientes = [
        {'nome': "Mario Silva de Carvalho", 'idade': '44 anos', 'nascimento': '17/08/1982'},
        {'nome': "Jose Alves", 'idade': '42 anos', 'nascimento': '17/08/1980'},
        {"nome": "Ana Maria Braga", "idade": 35, "nascimento": "10/12/1988"}
    ]
    return render(request, 'clientes/dados_clientes.html', {'titulo': titulo, 'dados_clientes':nossos_clientes})

def fomrulario(request):
    titulo = "Nosos Clientes"
    return render(request, 'clientes/form.html', {'titulo':titulo})

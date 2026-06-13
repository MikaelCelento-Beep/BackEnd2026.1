from django.shortcuts import render
from .models import Alunos, Conta
# Create your views here.

def home(request):
    titulo = "Página Inicial"
    return render(request, 'cadastro/home.html', {'titulo': titulo})

def formulario(request):
    titulo = "Cadastro Alunos"
    return render(request, 'cadastro/form.html', {'titulo':titulo})

def cadastro_alunos(request):
    pagina = "Informações dos Alunos"

    lista_alunos = Alunos.objects.all()

    return render(request, 'cadastro/alunos.html', {'msg':pagina, 'lista': lista_alunos })

def contato(request):
    titulo = "Contato"
    contato = "email@python.com"
    return render(request, 'cadastro/contato.html', {'titulo': titulo, 'contato': contato})

def conta(request):
    titulo = "Contas Pessoas Físicas"
    nossas_contas = Conta.objects.all()
    return render(request, 'cadastro/dados_contas.html', {'titulo': titulo, 'contas':nossas_contas})
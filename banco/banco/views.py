from django.shortcuts import render

# Create your views here.

#Função da página inicial
def index(request):
    return render(request, 'pages/home.html')

#função para abrir conta 
def abrir_conta(request):
    return render(request, 'pages/abrir_conta.html')

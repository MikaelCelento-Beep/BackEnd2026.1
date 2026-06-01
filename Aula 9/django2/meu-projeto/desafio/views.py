from django.shortcuts import render

# Create your views here.

def cadastro_alunos(request):
    pagina = "Informações dos Alunos"

    lista_alunos = [
        {'nome': 'Pedro Henrique', 'idade': '47 anos', 'nascimento': '26/05/1979', 'curso': 'Direito', 'turma': '105'}, 
        {'nome': 'Guilherme Guimarães', 'idade': '36 anos', 'nascimento': '22/06/1989', 'curso': 'Enfermagem', 'turma': '101'},
        {'nome': 'Gabriel Oliveira', 'idade': '26 anos', 'nascimento': '02/04/2000', 'curso': 'Engenharia Civil', 'turma': '103'},
        {'nome': 'Son Goku', 'idade': '46 anos', 'nascimento': '08/05/1979', 'curso': 'Educação Física', 'turma': '104'},        
        {'nome': 'Gustavo Andrade', 'idade': '27 anos', 'nascimento': '02/08/1999', 'curso': 'Ciência de Dados', 'turma': '102'}
    ]

    return render(request, 'cadastro/alunos.html', {'msg':pagina, 'lista': lista_alunos })
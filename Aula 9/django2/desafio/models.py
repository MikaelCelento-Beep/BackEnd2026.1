from django.db import models

# Create your models here.

class Campus(models.Model):
    unidade = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campus"

    def __str__(self):
        return self.unidade

class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    nascimento = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)
    turma = models.CharField(max_length=14)

    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
    
    def __str__(self):
        return self.nome


class Conta(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=30, unique=True)
    cliente = models.ForeignKey(Alunos, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero



from django.contrib import admin

# Register your models here.
from .models import Alunos, Conta, Campus

admin.site.register(Alunos)
admin.site.register(Conta)
admin.site.register(Campus)


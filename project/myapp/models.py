# pylint: disable=E1101

from django.db import models
from typing import Type
from django.shortcuts import render



class Soma(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    resultado = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.num1} + {self.num2} = {self.resultado}'

def soma(request):
    valor1 = int(request.GET.get('valor1', 0))
    valor2 = int(request.GET.get('valor2', 0))
    resultado = valor1 + valor2
    
    # cria uma nova instância do modelo Soma.
    resultadosoma = Soma(num1=valor1, num2=valor2, resultado=resultado)
    
    # salva a instância no banco de dados
    resultadosoma.save()

    return render(request, 'soma.html', {'resultado': resultado})

from django.shortcuts import render
from myapp.models import Soma

# Create your views here.

def home(request):
    return render(request, 'home.html')


def somar(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        resultado = num1 + num2
        soma = Soma(num1=num1, num2=num2, resultado=resultado)
        soma.save()
        return render(request, 'resultado.html', {'resultado': resultado})
    else:
        return render(request, 'home.html')
    
def lista_somas(request):
    somas = Soma.objects.all()
    return render(request, 'lista_somas.html', {'somas': somas})

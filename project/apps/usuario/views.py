from django.shortcuts import render

# Create your views here.

from .models import Usuario

def home (request):
    usuarios_registrados = Usuario.objects.all()
    contexto = {"usuarios" : usuarios_registrados}
    return render(request, "usuario/index.html", contexto) 
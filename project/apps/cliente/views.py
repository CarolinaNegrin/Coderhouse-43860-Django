from django.shortcuts import render, redirect

# Create your views here.
from .models import Cliente, Pais
from .forms import ClienteForm
from datetime import date
def home(request):
    clientes_registros = Cliente.objects.all()
    contexto =  {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "cliente/index.html", contexto)

def crear_clientes(request):
    
    p1 = Pais(nombre="Perú")
    p2 = Pais(nombre="Argentina")
    p3 = Pais(nombre="Italia")
    p1.save()
    p2.save()
    p3.save()

    c1 = Cliente(nombre="Almendra", apellido="Ruiseñor", nacimiento=date(2001,1,1), pais_origen_id=p1)
    c2 = Cliente(nombre="Pepe", apellido="Argento", nacimiento=date(1960,5,2), pais_origen_id=p2)
    c3 = Cliente(nombre="Carmella", apellido="Miranda", nacimiento=date(1993,1,7),pais_origen_id=None)
    c4 = Cliente(nombre="Alexander", apellido="Miranda", nacimiento=date(1990,9,9),pais_origen_id=p3)

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    
    return redirect("cliente:home")

def crear_cliente(request) :
    if request.method == "POST" :
        form = ClienteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("cliente:home")
    else: #request.method == "GET"
        form = ClienteForm()
    return render(request, "cliente/crear.html",{'form':form} )
    
def busqueda(request):
    #Busqueda por nombre que contenga "al"
    cliente_nombre = Cliente.objects.filter(nombre__contains="al")
    #Busqueda por año nacimiento mayor a 2000
    cliente_nacimiento = Cliente.objects.filter(nacimiento__gt=date(2000,1,1))
    #Pais de origen vacío
    cliente_pais = Cliente.objects.filter(pais_origen_id=None)

    contexto = {"cliente_nombre":cliente_nombre,
                "cliente_nacimiento": cliente_nacimiento,
                "cliente_pais":cliente_pais}
    return render(request, "cliente/busqueda.html", contexto)

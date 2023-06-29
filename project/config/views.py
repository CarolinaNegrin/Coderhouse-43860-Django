from datetime import datetime

from django.http import HttpResponse
<<<<<<< HEAD
from django.template import Context, Template
from datetime import datetime
from django.shortcuts import render
=======
from django.shortcuts import render

# from django.template import Context, Template

>>>>>>> cb96a39ef72a5a2d840bafb3a7ef5818444326f4

def saludo(request):
    return HttpResponse("Hola Django - Coder")


def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h1>")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")


def probando_template(request):
<<<<<<< HEAD
	# mi_html = open("./templates/template1.html")
	# mi_template = Template(mi_html.read())
	# mi_html.close()
	nombre = "Louis" #! nuevo
	apellido ="Van Beethoven" #! nuevo 
	ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #! nuevo
	datos = {"nombre": nombre, "apellido": apellido} #! nuevo
	datos["fecha"]= ahora
	# mi_contexto = Context(datos) #! cambio
	# mi_contexto = Context()
	# mi_documento = mi_template.render(mi_contexto)
	# return HttpResponse(mi_documento)
	return render(request, "template1.html", datos)

def fecha_hora (request):
	
	ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	return HttpResponse(f"<h1> Fecha y hora: {ahora} </h1>")

def mis_notas(request):
	notas =[10, 6, 3, 2]
	diccionario = {"notas": notas}
	return render(request, "mis_notas.html", diccionario)

def hobbies(request):
	hobbies =["Pintar", "Bailar", "Cantar"]
	respuesta = {"hobbies": hobbies}
	return render(request, "hobbies.html", respuesta)
=======
    nombre = "Louis"
    apellido = "Van Beethoven"
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:S.%f")
    datos = {"nombre": nombre, "apellido": apellido}
    datos["fecha"] = ahora
    return render(request, "template1.html", datos)


def fecha_hora(request):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:S.%f")
    return HttpResponse(f"<h1> ⌛ Fecha y hora: {ahora} </h1>")


def mis_notas(request):
    lista_de_notas = [2, 3, 5, 7, 9, 10, 10]
    contexto = {"notas": lista_de_notas}
    return render(request, "notas.html", contexto)


def diccionario(request):
    mi_diccionario = {"persona": {"nombre": "Cintia", "edad": 38}}

    return render(request, "prueba.html", mi_diccionario)
>>>>>>> cb96a39ef72a5a2d840bafb3a7ef5818444326f4

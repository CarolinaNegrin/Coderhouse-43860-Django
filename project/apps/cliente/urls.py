from django.urls import path

from .views import home, crear_clientes, crear_cliente, busqueda

app_name = "cliente"       

urlpatterns = [
    path("", home, name="home" ),
    path("crear_clientes", crear_clientes, name="crear_clientes"),
    path("crear_cliente", crear_cliente, name="crear_cliente"),
    path("busqueda/", busqueda, name="busqueda"),   
]


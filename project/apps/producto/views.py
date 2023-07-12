from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

# PAGINA PRINCIPAL


# def index(request):
#     return render(request, "producto/index.html")


# list
# def productocategoria_list(request):
#     categorias = models.ProductoCategoria.objects.all()
#     context = {"object_list": categorias}
#     return render(request, "producto/productocategoria_list.html", context)

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria


# create
# def productocategoria_create(request):
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:home")
#     else:
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_form.html", {"form": form})

class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# detail
# def productocategoria_detail(request, pk):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     return render(request, "producto/productocategoria_detail.html", {"object": query})

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria

# update
# def productocategoria_update(request, pk):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST, instance=query)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:home")
#     else:
#         form = forms.ProductoCategoriaForm(instance=query)
#     return render(request, "producto/productocategoria_form.html", {"form": form})


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# def productocategoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_confirm_delete.html", {"object": query})

class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")

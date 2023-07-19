from django.contrib import admin

from . import models

admin.site.site_title = "Productos"

# admin.site.register(models.ProductoCategoria)


@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "categoria_id",
        "nombre",
        "unidad_medida",
        "cantidad",
        "descripcion",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("categoria_id", "nombre")
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_actualizacion"

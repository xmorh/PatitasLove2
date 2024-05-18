from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "marca", "precio"]
    list_editable = ["nombre", "marca", "precio"]
    search_fields = ["id", "nombre", "marca", "precio"]
    list_filter = ["id", "nombre", "marca", "precio"]
    
admin.site.register(Producto, ProductoAdmin)


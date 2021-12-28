from django.contrib import admin

from core.models import Categoria, Compra, Distribuidora, ItensCompra, Marca, Racao

admin.site.register(Categoria)
admin.site.register(Compra)
admin.site.register(Distribuidora)
admin.site.register(Marca)
admin.site.register(Racao)
admin.site.register(ItensCompra)

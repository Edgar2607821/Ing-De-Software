from django.contrib import admin
from .models import Cliente, Venta, TipoDisp, Dispositivo, Marca, Modelo, Catalogo

# Register your models here.
class TipoDispInline(admin.TabularInline):
    model = TipoDisp

class MarcaInline(admin.TabularInline):
    model = Marca

class ModeloInline(admin.TabularInline):
    model = Modelo

class DispositivoAdmin(admin.ModelAdmin):
    inlines = [TipoDispInline]

class TipoDispAdmin(admin.ModelAdmin):
    inlines = [MarcaInline]

class MarcaAdmin(admin.ModelAdmin):
    inlines = [ModeloInline]

admin.site.register(TipoDisp)
admin.site.register(Dispositivo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Catalogo)
admin.site.register(Cliente)
admin.site.register(Venta)

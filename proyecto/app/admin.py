from django.contrib import admin
from .models import Genero,Distribuidora,Juego,Slider,Plataformas,Controles
# Register your models here.
class GeneroAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class DistribuidoraAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class JuegoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class SliderAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class PlataformasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class ControlesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Genero,GeneroAdmin)
admin.site.register(Distribuidora,DistribuidoraAdmin)
admin.site.register(Juego,JuegoAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Plataformas,PlataformasAdmin)
admin.site.register(Controles,ControlesAdmin)
# Register your models here.

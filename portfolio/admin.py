from django.contrib import admin
from .models import Linguagem
from .models import Projeto
from .models import Cadeira


# Register your models here.

class ProjetosHorizontal(admin.ModelAdmin):
    filter_horizontal = ('participantes',)

    class CadeirasHorizontal(admin.ModelAdmin):
        filter_horizontal = ('cadeiras',)

        admin.site.register(Linguagem)
        admin.site.register(Projeto)
        admin.site.register(Cadeira)

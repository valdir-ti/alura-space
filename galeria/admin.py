from django.contrib import admin
from galeria.models import Fotografia

'''Configurações da listagem de fotografias'''
'''list_display serve para mostrar os campos na listagem'''
'''list_display_links serve para indicar quais campos podemos abrir para edição'''
'''search_fields serve para definir quais campos podemos utilizar para realizar buscas'''
'''list filter: serve para definir um campo para filtrar por uma lista'''
'''list_per_page determina uma paginação e quantos itens devem aparecer por vez'''
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'foto')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', )
    list_per_page = (10)

admin.site.register(Fotografia, ListandoFotografias)
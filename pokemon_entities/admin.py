from django.contrib import admin

from .models import Pokemon, PokemonEntity


class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ("pokemon", "level", "health", "strength", "defence", "stamina")


admin.site.register(Pokemon)
admin.site.register(PokemonEntity, PokemonEntityAdmin)

admin.site.site_header = "Покемон БД"
admin.site.site_title = "Покемон БД"
admin.site.index_title = "Добро пожаловать в базу данных покемонов"

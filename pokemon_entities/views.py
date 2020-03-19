import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemons(request, folium_map, pokemon):
    for entity in pokemon.pokemon_entities.all():
        image_url = (
            request.build_absolute_uri(entity.pokemon.image.url) or DEFAULT_IMAGE_URL
        )
        icon = folium.features.CustomIcon(image_url, icon_size=(50, 50),)
        folium.Marker(
            [entity.latitude, entity.longitude],
            tooltip=entity.pokemon.title_ru,
            icon=icon,
        ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        add_pokemons(request, folium_map, pokemon)

    context = {"map": folium_map._repr_html_(), "pokemons": pokemons}

    return render(request, "mainpage.html", context=context)


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    try:
        pokemon = Pokemon.objects.get(pk=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    add_pokemons(request, folium_map, pokemon)

    context = {"map": folium_map._repr_html_(), "pokemon": pokemon}
    return render(request, "pokemon.html", context=context)

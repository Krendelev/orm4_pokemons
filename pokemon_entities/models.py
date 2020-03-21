from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=50, verbose_name="Название по-русски")
    title_en = models.CharField(
        max_length=50, verbose_name="Название по-английски", blank=True
    )
    title_jp = models.CharField(
        max_length=50, verbose_name="Название по-японски", blank=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    previous_evolution = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="next_evolutions",
        on_delete=models.SET_NULL,
        verbose_name="Из кого эволюционировал",
    )
    image = models.ImageField(upload_to="pokemon_images", verbose_name="Изображение")

    class Meta:
        verbose_name = "Вид покемона"
        verbose_name_plural = "Виды покемонов"

    def next_evolution(self):
        return self.next_evolutions.first()

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name="pokemon_entities",
        verbose_name="Вид покемона",
    )
    latitude = models.FloatField(blank=True, null=True, verbose_name="Широта")
    longitude = models.FloatField(blank=True, null=True, verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Появился", blank=True, null=True)
    disappeared_at = models.DateTimeField(verbose_name="Исчез", blank=True, null=True)
    level = models.SmallIntegerField(verbose_name="Уровень", blank=True, null=True)
    health = models.SmallIntegerField(verbose_name="Здоровье", blank=True, null=True)
    strength = models.SmallIntegerField(verbose_name="Сила", blank=True, null=True)
    defence = models.SmallIntegerField(verbose_name="Защита", blank=True, null=True)
    stamina = models.SmallIntegerField(
        verbose_name="Выносливость", blank=True, null=True
    )

    class Meta:
        verbose_name = "Покемон"
        verbose_name_plural = "Покемоны"

    def __str__(self):
        return self.pokemon.title_ru

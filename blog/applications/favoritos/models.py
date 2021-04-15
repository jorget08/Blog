from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry
from .managers import FavoritesManager


class Favorites(TimeStampedModel):
    """ Modelo para favotios """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()

    class Meta:

        #Para que un usuario no pueda agregar varias veces el mismo articulo a favoritos sino una sola vez
        #El unique_together es el que hace que no se pueda crear un nuevo objeto si ya existe ese usuario con esa entrada
        unique_together = ('user', 'entry')

        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'
    
    def __str__(self):
        return self.entry.title

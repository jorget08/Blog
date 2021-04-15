from django.db import models

#Third apps
from model_utils.models import TimeStampedModel #Es para que integre de una la fecha de creacion y la de modificacion de
                                                #un registro en el modelo en el que lo pongamos
# Create your models here.

class Home(TimeStampedModel):
    title = models.CharField(max_length=30)
    description = models.TextField(default='a')
    about_title= models.CharField(max_length=50)
    about_text = models.TextField(default='a')
    contact_email = models.EmailField(blank=True, null=True)

    phone = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):

    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    messagged = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name
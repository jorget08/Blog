from datetime import timedelta, datetime

from django.urls import reverse_lazy
from django.contrib.sitemaps import Sitemap

from applications.entrada.models import Entry

class EntrySitemap(Sitemap):

    # frecuencia con la que realizamos cambios sobre las urls que pertenecen a este sitemap
    changefreq = "weekly" # Si es nunca se puede poner -> "never"

    # Prioridad
    priority = 0.8

    protocol = "https"

    #Sobre escribimos esta funcion
    def items(self):
        return Entry.objects.filter(public = True)

    # funcion para poner el orden en el que se quiere poner, en este caso en e cronologico
    def lastmod(self, obj):
        return obj.created


# Tenemos que redefinir el sitemap SIEMPRE
class Sitemap(Sitemap):
    protocol = 'https'

    """Django nos pide que pongamos estas funciones al redefinir Sitemap"""
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'
    
    def lastmod(self, obj):
        return datetime.now()
    
    def location(self, obj):
        return reverse_lazy(obj)

"""A demas debemos redefinir las urls del projecto, no de la application
   Tambien poner la funcion def get_absolute_url en el models del que se esta trabajando el sitemap
   Y por ultimo agregarlo en el base.py en las applicaciones"""
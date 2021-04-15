from django.db import models


class EntryManager(models.Manager):


    def entrada_en_portada(self):
        return self.filter(
            public = True,
            portada = True,
                    #created que viene en el modelo por el TimeStampedModel
        ).order_by('-created').first() #first nos va a traer el primero que encuentra en la busqueda

    def entradas_en_home(self):
        return self.filter(
            public = True,
            in_home = True
        ).order_by('-created')[:4] #que me retorne los primeros 4 


    def entradas_recientes(self):
        return self.filter(
            public = True
        ).order_by('-created')[:6] #que me retorne las ultimas 6 creadas


    def buscar_entrada(self, kword, categoria):

        #verificamos que si envian categoria o no
        if len(categoria) > 0:
            return self.filter(
                #recordar que estamos en el modelo Entry; category es el foreginkye con el modelo Category al que
                #accedemos a su short_name
                category__short_name = categoria,
                title__icontains = kword,
                public = True
            ).order_by('-created')

        else:
            return self.filter(
                title__icontains=kword,
                public = True
            ).order_by('-created')
from django.db import models

class FavoritesManager(models.Manager):

    def user_profile(self, usuario):
        return self.filter(
            entry__public = True,
            user = usuario
        ).order_by('-created')
from django.urls import path
from . import views

app_name = 'favoritos'

urlpatterns = [
    path(
        route = 'perfil/',
        view = views.UserPageView.as_view(),
        name = 'perfil'
    ),
    path(
        route = 'add-entrada/<pk>/',
        view = views.AddFavoritesView.as_view(),
        name = 'add-favoritos'
    ),
    path(
        route = 'delete-favorites/<pk>/',
        view = views.FavoritesDeleteView.as_view(),
        name = 'delete-favoritos'
    ),
]
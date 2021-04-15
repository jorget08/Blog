from django.urls import path
from . import views

app_name = 'entrada'

urlpatterns = [
    path(
        route = 'entradas/',
        view = views.EntryListView.as_view(),
        name = 'lista_entradas'
    ),
    path(# este slug hace referencia al campo del modelo(todo gracias a la def save que hicimos en el modelo)
        route = 'entrada/<slug>/',
        view = views.EntryDetailView.as_view(),
        name = 'detail'
    ),
]
#
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path(
        route = '', 
        view = views.HomePageView.as_view(),
        name='index',
    ),
    path(
        route = 'register-suscription', 
        view = views.SuscribersCreateView.as_view(),
        name='add-suscribe',
    ),
    path(
        route = 'contact', 
        view = views.ContactCreateView.as_view(),
        name='add-contact',
    ),     
]
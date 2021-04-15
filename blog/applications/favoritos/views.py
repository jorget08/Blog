from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View, DeleteView

from applications.entrada.models import Entry
from .models import Favorites
# Create your views here.


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'favoritos'
    success_url = reverse_lazy('home:index')

    #redireccion para quien no este logueado
    login_url = reverse_lazy('users:user-login')

    def get_queryset(self):
        
        return Favorites.objects.user_profile(self.request.user)


class AddFavoritesView(LoginRequiredMixin, View):
    #redireccion para quien no este logueado
    login_url = reverse_lazy('users:user-login')

    #La vista View que es la mas generica de todas nos permite denifir el metodo get y el post para que se realice
    #la accion que queremos
    def post(self, request, *args, **kwargs):
        usuario = self.request.user

        #recuperamos el id o pk del blog que queremos añadir a favoritos(se recupera por la url)
        entrada = Entry.objects.get(id=self.kwargs['pk'])

        Favorites.objects.create(
            user = usuario,
            entry = entrada,
        )
        return HttpResponseRedirect(reverse('favoritos:perfil',))



class FavoritesDeleteView(LoginRequiredMixin, DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos:perfil',)

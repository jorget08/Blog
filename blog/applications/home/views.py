import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, CreateView
from applications.entrada.models import Entry
from .models import Home
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        """como contexto se puede enviar lo que sea, un formulario, una lista, un diccionario, etc"""

        # Para los articulos que se van a mostrar en el index
        context['portada'] = Entry.objects.entrada_en_portada()
        context['home'] = Entry.objects.entradas_en_home()
        context['recientes'] = Entry.objects.entradas_recientes()

        # Para la seccion de info
        context['sobre_nosotros'] = Home.objects.latest('created')

        #Envio de formulario de suscripcion
        context['form_de_sub'] = SuscribersForm

        return context
    

"""Clase para el formulario de suscripcion"""
class SuscribersCreateView(CreateView):
    
    #Como ya se esta usando dentro de la pag index pues no necesita template_name

    form_class = SuscribersForm
    success_url = '.'


"""Clase para el formulario del footer"""

class ContactCreateView(CreateView):
    """Como este se presenta en varias paginas, para no tener que añadir el contexto en cada vista en la 
    que aparezca el footer lo que hacemos es arreglar al footer.hmtl de forma manual editando las etiquetas
    input poniendoles el name y el id"""

    form_class = ContactForm
    success_url = '.'


"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include
#Importacion para poder cargar las imagenes
from django.conf import settings
from django.conf.urls.static import static
#SEO
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.entrada.urls')),
    re_path('', include('applications.favoritos.urls')),
    #url para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Generar el XML
sitemaps = {
    'site':Sitemap(
        [
            'home:index'
        ]
    ),
    'entradas': EntrySitemap
}

# Url para el xml
urlpatterns_sitemap = [
    path(
        #Podemos revisarlo en el /sitemap.xml
        'sitemap.xml', 
        sitemap, 
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap
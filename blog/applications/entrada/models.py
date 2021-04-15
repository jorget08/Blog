from datetime import timedelta, datetime

from django.db import models
#Traemos de nuestra configuracion el user ya que nosotros lo cambiamos personalizandolo
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy


#Third apps
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#Local
from .managers import EntryManager

# Create your models here.


class Category(TimeStampedModel):

    short_name = models.CharField(max_length=15, unique=True)

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    
class Tag(TimeStampedModel):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name



class Entry(TimeStampedModel):

    #Nuestro modelos de usuario personalizado
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')

    #ckeditor
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen', 
        upload_to='Entry',
    )
    # Este campo es que el articulo va en la portada o no(el articulo mas top ps)
    portada = models.BooleanField(default=False)
    # Este campo es que va en la pag principal( los otros 4 mas tops en nuestro caso)
    in_home = models.BooleanField(default=False)

    #exclusivamente para el SEO
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title


    # Funcion que podemos sobre escribir en lo modelos para que cuando se guarde algo de este modelo
    # ocurra una accion que queremos(por ej: que al guardar un prestamo, se descuente un libro en el stock)
    def save(self, *args, **kwargs):

        now = datetime.now()
        total_time = timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        seconds = int(total_time.total_seconds())

        #concatenamos el titulo del articulo y los segundos que generamos
        slug_unique = '%s %s' % (self.title, str(seconds))

        # los self.title y self.slug son los campos que tiene el modelo Entry (en el que estamos trabajando)
        self.slug = slugify(slug_unique)

        super().save(*args, **kwargs)

    
    # SEO
    def get_absolute_url(self):
        return reverse_lazy(
            'entrada:detail',
            kwargs={
                'slug': self.slug
            }
        )
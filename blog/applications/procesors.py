from applications.home.models import Home

# Procesor para recuperar telefono y correo del registro home para

# Los procesors son siempre funciones, pueden ser clases pero deben retornar una funcion
def home_contact(request):
    home = Home.objects.latest('created')

    #Siempre en procesor debemos retornar un diccionario 
    return {
        # la clave como quereos llamarla, y el valor sera la variable del modelo que queremos recuperar
        'phone' : home.phone,
        'correo' : home.contact_email,
    }

"""AHORA SE AÑADE EN EL BASE.PY EN LA PARTE DE TEMPLATES EN EL: context_processors"""
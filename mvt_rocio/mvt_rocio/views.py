from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def fecha_actual(request):
    hoy=datetime.now().strftime("%d|%m|%Y")
    return HttpResponse(f"Fecha actual: {hoy}")



def datos_familiares(request):

    archivo = open("/Users/Rocio/Coderhouse/MVT_Rocio/mvt_rocio/mvt_rocio/templates/mvt.html")

    #cramos el template y le pasamos el cont de archivo
    plantilla = Template(archivo.read())

    #cerramos archivo 
    archivo.close()

    informacion_nombre = ['Nombre: Ana',
     'Nombre: Omar',
     'Nombre: Lucia'
    ]

    informacion_edad = ['Edad: 58',
    'Edad: 56',
    'Edad: 25'
    ]

    datos = {'informacion': informacion_nombre,'Edad': informacion_edad}

    #creamos el contexto
    contexto = Context(datos)

    #creamos el doc

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
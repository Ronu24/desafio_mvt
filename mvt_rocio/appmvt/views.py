from django.http import HttpResponse

from appmvt.models import familia

# Create your views here.

def listado_de_familia(request):
    listado = familia.objects.all()

    Vista = ""
    for FAMILIA in listado:
        Vista += f"({FAMILIA.nombre},{FAMILIA.edad})" + " | "

    return HttpResponse(Vista)

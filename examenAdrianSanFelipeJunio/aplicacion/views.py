from django.shortcuts import render
from aplicacion.models import Usuario, Fichero, Acceso
from django.http import HttpResponse

def index(request):

    error = None

    #Lista con los accesos del usuario 1001
    usuario1001 = Usuario.objects.get(id=1001)
    acceso_usuario1001 = Acceso.objects.filter(usuario=1001)
    context_dict = {}
    context_dict['nombreU'] = usuario1001.nombreU
    context_dict['accesos'] = acceso_usuario1001
    context_dict['error'] = error

    if acceso_usuario1001 is None:
        error = "No hay fichero del usuario 1001"
        context_dict['error'] = error

    return render(request, 'aplicacion/usuario.html', context_dict)

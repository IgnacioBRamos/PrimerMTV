from multiprocessing import context
from django.shortcuts import render

from integrantes.models import Personas
# Create your views here.


def crear_persona(request):
    nueva_persona= Personas.objects.create(name="Carlos Alberto",surname="Sanchez",edad=65,nacimiento="1957-03-31")
    context = {
        "nueva_persona": nueva_persona
    }
    return render(request,"persona.html",context=context)

def lista_personas(request):
    personitas = Personas.objects.all()
    context = {
        "personas": personitas
    }
    return render(request,"personas_lista.html",context=context)
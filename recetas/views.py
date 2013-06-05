# Create your views here.
from recetas.models import Bebida
from django.shortcuts import render_to_response

def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    return render_to_response('lista_bebidas.html', {'bebidas':bebidas})

# Create your views here.
from recetas.models import Receta, Comentario
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def about(request):
    html = "<html><body>Proyecto de ejemplo en Django</html></body>"
    return HttpResponse(html)

def home(request):
    recetas = Receta.objects.all()
    return render_to_response('home.html', {'recetas':recetas})



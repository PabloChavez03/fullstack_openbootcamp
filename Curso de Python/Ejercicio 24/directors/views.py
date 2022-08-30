from django.shortcuts import render
from django.http import Http404

from .models import Director, Pelicula

# Create your views here.


def index(request):
    auxDirectores = Director.objects.all()

    peliculas = Pelicula.objects.all()
    print("Soy el idnex")

    return render(
        request,
        'index.html',
        context={
            'directores': auxDirectores.values(),
            'peliculas': peliculas
        }
    )


def detail(request, director_id):
    try:
        allPeliculas = Pelicula.objects.all().values()
        listPeliculas = []
        for pelicula in allPeliculas:
            if (pelicula['director_id'] == director_id):
                listPeliculas.append(pelicula)
    except Pelicula.DoesNotExist:
        raise Http404("No existen peliculas")

    return render(
        request,
        'detail.html',
        context={
            'peliculas': listPeliculas
        }
    )

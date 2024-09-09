from django.shortcuts import render

from datetime import datetime


from django.views import View

from blog.models import Movies


def movies_page(request,):
    user = request.user
    films = Movies.objects.all()

    return render(request, 'movies_page.html', {'user': user, "films": films})

def movies_one_page(request,one_m_id):
    user = request.user
    film = Movies.objects.filter(id=one_m_id).first()
    actors = film.actors.all()
    directors = film.directors.all()

    return render(request, 'one_movies_page.html', {'user': user, "film": film, "actors": actors, "directors": directors})


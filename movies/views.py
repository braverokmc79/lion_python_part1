from django.shortcuts import render, get_object_or_404
from .models import Movie



# Create your views here.
def index(request):
    return render(request, 'index.html')


def movie_list(request):
    return render(request, 'movies/movie_list.html')



def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})




def str_page(request, id):
    return render(request, 'movies/str_page.html', {'id': id})









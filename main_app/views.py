from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Anime


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animes_index(request):
    animes = Anime.objects.all()
    return render(request, 'animes/index.html', {
        'animes': animes
    })

def animes_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'animes/detail.html', {
        'anime': anime
    })

class AnimeCreate(CreateView):
  model = Anime
  fields = '__all__'

class AnimeUpdate(UpdateView):
  model = Anime
  fields = ['title', 'genre', 'description']

class AnimeDelete(DeleteView):
  model = Anime
  success_url = '/animes'
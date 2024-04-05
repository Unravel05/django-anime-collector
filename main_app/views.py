from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Anime, Streamer
from .forms import PhasingForm

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
    id_list = anime.streamer.all().values_list('id')
    streamers_anime_doesnt_have = Streamer.objects.exclude(id__in=id_list)
    phasing_form = PhasingForm()
    return render(request, 'animes/detail.html', {
        'anime': anime, 'phasing_form': phasing_form,
         'streamer': streamers_anime_doesnt_have
    })

class AnimeCreate(CreateView):
  model = Anime
  fields = ['title', 'genre', 'description', 'rate']

class AnimeUpdate(UpdateView):
  model = Anime
  fields = ['title', 'genre', 'description', 'rate']

class AnimeDelete(DeleteView):
  model = Anime
  success_url = '/anime'

def add_phasing(request, anime_id):
  # create a ModelForm instance using the data in request.POST
  form = PhasingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_phasing = form.save(commit=False)
    new_phasing.anime_id = anime_id
    new_phasing.save()
  return redirect('detail', anime_id=anime_id)


class StreamerList(ListView):
  model = Streamer

class StreamerDetail(DetailView):
  model = Streamer

class StreamerCreate(CreateView):
  model = Streamer
  fields = '__all__'

class StreamerUpdate(UpdateView):
  model = Streamer
  fields = ['name', 'device']

class StreamerDelete(DeleteView):
  model = Streamer
  success_url = '/streamers'

def assoc_streamer(request, anime_id, streamer_id):
    Anime.objects.get(id=anime_id).streamer.add(streamer_id)
    return redirect('detail', anime_id=anime_id)

def unassoc_streamer(request, anime_id, streamer_id):
    Anime.objects.get(id=anime_id).streamer.remove(streamer_id)
    return redirect('detail', anime_id=anime_id)


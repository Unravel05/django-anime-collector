from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name='about'),
    path('animes/', views.animes_index, name= 'index'),
    path('animes/<int:anime_id>', views.animes_detail, name='detail'),
    path('animes/create', views.AnimeCreate.as_view(), name='animes_create'),
    path('animes/<int:pk>/update/', views.AnimeUpdate.as_view(), name='animes_update'),
    path('animes/<int:pk>/delete/', views.AnimeDelete.as_view(), name='animes_delete'),
    path('animes/<int:anime_id>/add_phasing/', views.add_phasing, name='add_phasing'),
    path('animes/<int:anime_id>/assoc_streamer/<int:streamer_id>/', views.assoc_streamer, name='assoc_streamer'),
    path('animes/<int:anime_id>/unassoc_streamer/<int:streamer_id>/', views.unassoc_streamer, name='unassoc_streamer'),
    path('streamers/', views.StreamerList.as_view(), name='streamers_index'),
    path('streamers/<int:pk>/', views.StreamerDetail.as_view(), name='streamers_detail'),
    path('streamers/create/', views.StreamerCreate.as_view(), name='streamers_create'),
    path('streamers/<int:pk>/update/', views.StreamerUpdate.as_view(), name='streamers_update'),
    path('streamers/<int:pk>/delete/', views.StreamerDelete.as_view(), name='streamers_delete'),
]
from django.urls import path
from .views import song_list, song_detail, add_song

urlpatterns = [
    path('', song_list, name='song_list'),
    path('<int:song_id>/', song_detail, name='song_detail'),
    path('add/', add_song, name='add_song'),
   
]

handler404 = 'TuneTracker.views.handler404'

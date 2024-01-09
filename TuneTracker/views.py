from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtistForm, SongForm
from .models import Artist, Song
from django.db.models import Count


def song_list(request):
    songs = Song.objects.all()
    artists_with_song_count = Artist.objects.annotate(song_count=Count('song'))

    all_artists = Artist.objects.all()  # Fetch all artists

    context = {
        'songs': songs,
        'artists_with_song_count': artists_with_song_count,
        'all_artists': all_artists,  
    }

    return render(request, 'TuneTracker/song_list.html', context)

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'TuneTracker/song_detail.html', {'song': song})

def home(request):
    return redirect('song_list')

def add_song(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'song':
            song_form = SongForm(request.POST)
            if song_form.is_valid():
                new_song = song_form.save()
                return redirect('song_list')
        elif form_type == 'artist':
            artist_form = ArtistForm(request.POST)
            if artist_form.is_valid():
                new_artist = artist_form.save()
                return redirect('song_list')
    else:
        artist_form = ArtistForm()
        song_form = SongForm()

    return render(request, 'TuneTracker/add_song.html', {'artist_form': artist_form, 'song_form': song_form})

def handler404(request, exception):
    return render(request, '404.html', status=404)
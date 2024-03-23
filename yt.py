from pytube import Playlist, YouTube
import os

urls = []
PATH = r"C:\Users\devmm\Desktop\Album"
URL = input('>>\n')

def download_music(stream, path):
    music = stream.streams.filter(only_audio=True)
    music_name = stream.title.split(' ')[0]

    print(f'Downloading... {music_name} - {yt.author}')

    music[0].download(path)
    print(yt.title + 'Downloaded!')


if 'playlist' in URL:
    playlist = Playlist(URL)
    playlist_name = playlist.title.split('-')[0]

    
    try:
        path = f'{PATH}\\{playlist_name}'
        os.mkdir(path)
    except FileExistsError:
        choice = input("You already downloaded this playlist, want to continue? y/n \n")
        if choice == 'y':
            path = f'{PATH}\\{playlist_name}'
        else:
            "Ended loop"
    
    for url in playlist:
            yt = YouTube(url)
            download_music(yt,path)

# is a music
else:
    yt = YouTube(URL)
    
    download_music(yt, PATH)

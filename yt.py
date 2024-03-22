from pytube import Playlist, YouTube
import os

urls = []
def download_music(item, caminho):
    # download
    out_file = item[0].download(caminho)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + 'Downloaded!')


# path directory download
PATH = r"C:\Users\devmm\Desktop\Album"

# Get url of download
URL = input('>>\n')

# if is a playlist
if 'playlist' in URL:
    # assign playlist
    playlist = Playlist(URL)
    print(f'Downloading: {playlist.title}')
    print('Number of Musics: %s' % len(playlist.video_urls))
    artist = playlist.title.split(' ')[0]

    # get all urls from playlist
    for url in playlist:
        urls.append(url)

    for url in urls:
        yt = YouTube(url)
        print(f'Starting Download... {yt.title}')
        music = yt.streams.filter(only_audio=True)

        # tenta criar uma pasta com o titulo da playlist
        try:
            new_dir = f'{PATH}\{artist}'
            path = os.mkdir(new_dir)
            download_music(music, path)
            
        except FileExistsError:
            path = f'{PATH}\{artist}'
            download_music(music, path)

    

# se for uma musica
else:
    pass


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
    print(f'Downloading Playlist: {playlist.title}')
    print('Number of Musics: %s' % len(playlist.video_urls))
    playlist_name = playlist.title.split(' ')[0]

    # get all urls from playlist
    for url in playlist:
        urls.append(url)

    for url in urls:
        yt = YouTube(url)
        print(f'Starting Download... {yt.title}')
        music = yt.streams.filter(only_audio=True)

        path = f'{PATH}\\{playlist_name}'

        # try create a directory with the playlist name
        try:
            path = os.mkdir(path)
            download_music(music, path)
            
        except FileExistsError:
            choice = input("You already downloaded this playlist, want to continue? y/n \n")
            if choice == 'y':
                download_music(music, path)
            else:
                break

    

# if is only 1 music
else:
    #URL
    yt = YouTube(str(URL))
    music = yt.streams.filter(only_audio=True)
    music_name = yt.title.split(' ')[0]

    path = PATH

    print(f'Downloading.... {music_name} - {yt.author}')
    out_file = music[0].download(path)
    base, ext = os.path.splitext(out_file)
    new_file = f'{music_name} - {yt.author}' + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + 'Downloaded!')
    print(f'{music_name} - {yt.author} has been downloaded!')


from pytubefix import Playlist, YouTube
import os
import sys

DOWNLOADS_DIR = os.path.join(os.path.dirname(__file__), 'downloads')

def download_audio(yt, path):
    """Downloads the best audio-only stream for a given YouTube object."""
    try:
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        if not audio_stream:
            print(f"No audio stream found for {yt.title}")
            return

        print(f'Downloading... {yt.title} - {yt.author}')
        audio_stream.download(output_path=path)
        print(f'{yt.title} Downloaded!')
    except Exception as e:
        print(f"An error occurred while downloading {yt.title}: {e}")

def main():
    """Main function to handle URL input and download."""
    if len(sys.argv) < 2:
        print("Usage: python yt.py <YOUTUBE_URL>")
        sys.exit(1)

    url = sys.argv[1]

    if not os.path.exists(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)

    if 'playlist' in url:
        playlist = Playlist(url)
        # Sanitize playlist title for folder name
        playlist_name = "".join([c for c in playlist.title if c.isalpha() or c.isdigit() or c.isspace()]).rstrip()
        playlist_path = os.path.join(DOWNLOADS_DIR, playlist_name)

        if not os.path.exists(playlist_path):
            os.makedirs(playlist_path)
        else:
            choice = input(f"Playlist '{playlist_name}' folder already exists. Continue? (y/n): ").lower()
            if choice != 'y':
                print("Operation cancelled.")
                return

        print(f"Downloading playlist: {playlist.title}")
        for video_url in playlist.video_urls:
            try:
                yt = YouTube(video_url)
                download_audio(yt, playlist_path)
            except Exception as e:
                print(f"Failed to get video info for {video_url}: {e}")
        print("Playlist download completed.")
    else:
        try:
            yt = YouTube(url)
            download_audio(yt, DOWNLOADS_DIR)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
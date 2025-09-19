from pytubefix import Playlist, YouTube
import os
import sys
import certifi
import ffmpeg

# Set SSL_CERT_FILE to certifi's certificate bundle
os.environ['SSL_CERT_FILE'] = certifi.where()

DOWNLOADS_DIR = os.path.join(os.path.dirname(__file__), 'downloads')

def download_audio(yt, path, convert_to_mp3=False):
    """Downloads the best audio-only stream for a given YouTube object."""
    try:
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        if not audio_stream:
            print(f"No audio stream found for {yt.title}")
            return

        print(f'Downloading... {yt.title} - {yt.author}')
        original_filepath = audio_stream.download(output_path=path)
        print(f'{yt.title} Downloaded!')

        if convert_to_mp3:
            print(f'Converting to MP3...')
            try:
                mp3_filepath = os.path.splitext(original_filepath)[0] + '.mp3'
                (
                    ffmpeg
                    .input(original_filepath)
                    .output(mp3_filepath)
                    .run(overwrite_output=True)
                )
                os.remove(original_filepath)
                print(f'Successfully converted to {mp3_filepath}')
            except ffmpeg.Error as e:
                print(f"An error occurred during conversion: {e.stderr.decode()}")
            except Exception as e:
                print(f"An error occurred during conversion: {e}")


    except Exception as e:
        print(f"An error occurred while downloading {yt.title}: {e}")

def download_video(yt, path):
    """Downloads the best progressive video stream for a given YouTube object."""
    try:
        video_stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        if not video_stream:
            print(f"No video stream found for {yt.title}")
            return

        print(f'Downloading... {yt.title} - {yt.author}')
        video_stream.download(output_path=path)
        print(f'{yt.title} Downloaded!')
    except Exception as e:
        print(f"An error occurred while downloading {yt.title}: {e}")

def main():
    """Main function to handle URL input and download."""
    if len(sys.argv) < 2:
        print("Usage: python yt.py <YOUTUBE_URL> [mp3/mp4/m4a]")
        sys.exit(1)

    url = sys.argv[1]
    download_format = 'm4a'
    if len(sys.argv) > 2:
        download_format = sys.argv[2].lower()

    if download_format not in ['mp3', 'mp4', 'm4a']:
        print("Invalid format. Please choose 'mp3', 'mp4', or 'm4a'.")
        sys.exit(1)

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
                if download_format == 'mp4':
                    download_video(yt, playlist_path)
                else:
                    convert_to_mp3 = (download_format == 'mp3')
                    download_audio(yt, playlist_path, convert_to_mp3=convert_to_mp3)
            except Exception as e:
                print(f"Failed to get video info for {video_url}: {e}")
        print("Playlist download completed.")
    else:
        try:
            yt = YouTube(url)
            if download_format == 'mp4':
                download_video(yt, DOWNLOADS_DIR)
            else:
                convert_to_mp3 = (download_format == 'mp3')
                download_audio(yt, DOWNLOADS_DIR, convert_to_mp3=convert_to_mp3)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
# YouTube Downloader

## About

This script downloads a YouTube video or playlist in various formats:
-   **mp4**: Video file with audio.
-   **m4a**: The best quality audio-only file (MPEG-4 Audio).
-   **mp3**: The audio is downloaded and then converted to MP3 format.

## Dependencies

*   [pytubefix](https://github.com/pytubefix/pytubefix)
*   [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
*   [certifi](https://github.com/certifi/python-certifi)


### FFmpeg Requirement

For converting audio to `.mp3`, this script uses `ffmpeg-python`, which relies on **FFmpeg**. You must have FFmpeg installed on your system for the `.mp3` conversion to work.

You can download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).

## Usage

1.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2.  Run the script with a YouTube URL:

    ```bash
    python yt.py <YOUTUBE_URL> [format]
    ```

    -   `<YOUTUBE_URL>`: The URL of the YouTube video or playlist.
    -   `[format]` (optional): The desired format (`mp4`, `mp3`, or `m4a`). Defaults to `m4a` if not specified.

    The files will be downloaded to the `downloads` directory.

## Development Notes

This script was originally written using the `pytube` library, but several issues were encountered during development.

### 1. SSL Certificate Verification Errors

The initial attempts to run the script resulted in `[SSL: CERTIFICATE_VERIFY_FAILED]` errors. This is a common issue on macOS where Python cannot find the root SSL certificates.

**Solution:** The script now programmatically sets the `SSL_CERT_FILE` environment variable to use the certificate bundle provided by the `certifi` library.

### 2. HTTP 400: Bad Request Errors

After fixing the SSL issue, the script encountered `HTTP Error 400: Bad Request` errors. This indicated that YouTube was rejecting the requests made by the `pytube` library. Research showed that the `pytube` library is not actively maintained and often falls behind YouTube's API changes.

**Solution:** The `pytube` library was replaced with `pytubefix`, a more actively maintained fork that is better at keeping up with YouTube's changes.

### 3. Video Unavailability and Login Errors

Even with `pytubefix`, some videos were unavailable due to geographic restrictions, age restrictions, or other policies requiring a user to be logged in. The library does not support authentication.

**Solution:** The script was tested with videos that do not have these restrictions, such as content from the YouTube Kids platform.
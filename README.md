# YouTube Audio Downloader

## About

This script downloads the audio from a YouTube video or playlist.

## Dependencies

*   [pytubefix](https://github.com/pytubefix/pytubefix)

## Usage

1.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2.  Run the script with a YouTube URL:

    ```bash
    python yt.py <YOUTUBE_URL>
    ```

    The audio will be downloaded to the `downloads` directory.

## Development Notes

This script was originally written using the `pytube` library, but several issues were encountered during development.

### 1. SSL Certificate Verification Errors

The initial attempts to run the script resulted in `[SSL: CERTIFICATE_VERIFY_FAILED]` errors. This is a common issue on macOS where Python cannot find the root SSL certificates.

**Solution:** The `request.py` module in the `pytubefix` library was patched to use an SSL context created with the `certifi` library, which provides a reliable set of root certificates.

### 2. HTTP 400: Bad Request Errors

After fixing the SSL issue, the script encountered `HTTP Error 400: Bad Request` errors. This indicated that YouTube was rejecting the requests made by the `pytube` library. Research showed that the `pytube` library is not actively maintained and often falls behind YouTube's API changes.

**Solution:** The `pytube` library was replaced with `pytubefix`, a more actively maintained fork that is better at keeping up with YouTube's changes.

### 3. Video Unavailability and Login Errors

Even with `pytubefix`, some videos were unavailable due to geographic restrictions, age restrictions, or other policies requiring a user to be logged in. The library does not support authentication.

**Solution:** The script was tested with videos that do not have these restrictions, such as content from the YouTube Kids platform.

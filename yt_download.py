import yt_dlp


def download_video():
    url = input("Enter the url of the video: ")
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Download complete")

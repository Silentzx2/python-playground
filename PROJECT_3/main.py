

import os  # File/folder related kaam ke liye
import yt_dlp  # YouTube videos download karne ke liye library

# Ye function live progress dikhata hai download ke time
def progress(d):

    # Bas ek message print hoga
    print("Downloading video...")

    # Agar video abhi download ho raha hai
    if d['status'] == 'downloading':

        # Kitna download hua bytes me
        download_progress = d.get('downloaded_bytes', 0)

        # Video ka total size bytes me
        total_size = d.get('total_bytes', 0)

        # Agar total size mil gaya
        if total_size > 0:

            # Downloaded bytes ko MB me convert karna
            mb_done = download_progress / 1024 / 1024

            # Total bytes ko MB me convert karna
            mb_total = total_size / 1024 / 1024

            # Progress print karna
            print(f"Downloaded: {mb_done:.2f} MB / {mb_total:.2f} MB")

    # Agar download complete ho gaya
    elif d['status'] == 'finished':

        # Completion message
        print("Download completed, now converting...")


# Main download function
def download_video():

    # Agar "videos" folder exist nahi karta
    if not os.path.exists("videos"):

        # To folder create kar do
        os.makedirs("videos")

    # Save path define karna
    save_path = "videos"

    # User se choice lena
    print("Which method do you want to use to download the video?")
    print("1. Single video")
    print("2. Multiple videos")

    # User input lena
    choice = input("Enter your choice (1 or 2): ")

    # Agar single video choose kiya
    if choice == "1":

        # Single URL input lena
        url = input("Enter the URL of the video you want to download: ")

    # Agar multiple videos choose kiya
    else:

        # Empty list banana URLs store karne ke liye
        urls = []

        # Infinite loop
        while True:

            # User se URL lena
            url = input(
                "Enter the URL of the video you want to download (or 'done' to finish): "
            )

            # Agar user "done" likhe
            if url == "done":

                # Loop break kar do
                break

            # URL list me add kar do
            urls.append(url)

    # yt-dlp settings dictionary
    youtube = {

        # Best quality download karna
        'format': 'bestvideo[height<=1080]+bestaudio/[abr<=320k]',

        # Output file ka path aur name
        'outtmpl': f"{save_path}/%(title)s.%(ext)s",

        # Progress function connect karna
        'progress_hooks': [progress]
    }

    # yt-dlp object create karna
    with yt_dlp.YoutubeDL(youtube) as ydl:

        # Agar single video option choose kiya
        if choice == "1":

            # Single video download
            ydl.download([url])

        # Agar multiple video option choose kiya
        else:

            # Multiple videos download
            ydl.download(urls)


# Ye check karta hai file directly run hui ya import hui
if __name__ == "__main__":

    # Download function run karna
    download_video()

    # Final success message
    print("Video downloaded successfully!")
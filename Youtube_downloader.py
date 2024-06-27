from pytube import Playlist,YouTube
from os import path

def download_video(playlist_url, output_path='.'):
    try:
        video=YouTube(playlist_url)
        print(f"Downloading {video.title}...")
        video.streams.filter(file_extension="mp4",progressive=True).first().download()
        print("Download completed!")
    except:
        print("There is some problem with the given URL")
        return;

def download_playlist(playlist_url, output_path='.'):
    try:
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            print(f"Downloading {video.title}...")
            video.streams.filter(file_extension="mp4", progressive=True).first().download()
        print("Download completed!")
    except:
        raise ValueError;

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    output_path = path.dirname
    print(output_path)
    try:
        if "playlist" in playlist_url:
            download_playlist(playlist_url, output_path)
        else :
            download_video(playlist_url,output_path)
    except ValueError:
        print("The given Url is not a playlist url")


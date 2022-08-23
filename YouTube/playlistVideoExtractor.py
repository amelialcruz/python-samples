#purpose: extract youtube playlist videos from specified playlist using var 'links'
#libraries
from pytube import YouTube
from pytube import Playlist

#define save path
SAVE_PATH = "C:/Desktop" #to_do


#link of the playlist to be downloaded
links= "https://www.youtube.com/playlist?list=OLAK5uy_nx1QFwTfdCN-spJ5BpaBsiNR8yxDxmZqk"

playlist = Playlist(links)

PlayListLinks = playlist.video_urls
N = len(PlayListLinks)

#playlist info
print(f"This playlist link has {N} videos.")
print(f"\n Downloading {N} videos...")

#downloading iteration
for i,link in enumerate(PlayListLinks):

    yt = YouTube(link)
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    d_video.download(SAVE_PATH)
    print(i+1, ' Video downloaded.')

#what song is my favorite off the playlist?
#purpose: download entire youtube playlist videos all at once

#libraries
import yt_download
import Playlist, YouTube

#sample playlist link
playlistLink = 'https://www.youtube.com/playlist?list=PLtdokPm7vPss1TXrV4gr2pnSXmMu-UFF4'
playlist = Playlist(playlistLink)

print('Number of videos in playlist: %s' % len(playlist.video_urls))

#iteration for each video url to download
for video_url in playlist.video_urls:
    yt = YouTube(video_url)

    #retrieve name/title of video (ex: The Weeknd - Dawn FM (Audio) )
    name = yt.title

    #replace space char w/ underscore in title name (ex: The_Weeknd_-_Dawn_FM_(Audio))
    yt_download(video_url, "{}.mp4".Format(name.replace(" ", "_")))

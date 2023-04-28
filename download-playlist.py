import re
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLuP7SQK7lt1beLieV5j3RziHL6WtiUVYQ')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    video.streams.first().download()

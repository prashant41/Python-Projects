# Download Only Video
"""from pytube import YouTube

link="https://www.youtube.com/watch?v=C3KRwfj9F8Q"
youtube_1=YouTube(link)

#print(youtube_1.thumbnail_url) Thumbnail image
#print(youtube_1.title)         Title 
#videos=youtube_1.streams.filter(only_audio=True) Only Audio

videos=youtube_1.streams.all()
vid=list(enumerate(videos))

for i in vid:
    print(i)
print()
strm=int(input("Enter :"))
videos[strm].download()
print('Succesfully Downloaded')"""

# Download playlist
from pytube import Playlist

py=Playlist(input("Enter the playlist Link:"))
print(f"Downloading :{py.title}")
for video in py.videos:
    video.streams.first().download()
print("Downloaded Succesfully")
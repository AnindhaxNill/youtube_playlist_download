import os
import sys

from pytube import Playlist, YouTube
import inquirer

pl = input("Enter your Youtube public playlist: ")
print(pl)

questions = [
    inquirer.List('format',
                  message="What Format do you need?",
                  choices=['audio', 'video'],
                  ),
]
answers = inquirer.prompt(questions)
print(answers["format"])

p = input("Enter your playlist save path: ")
print(p)

URL_PLAYLIST = pl

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
total_urls_found=f'Number Of Videos In playlist: {len(playlist.video_urls)}'
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)


# print(urls)
def download_audio_from_youtube(link, path):
    yt = YouTube(link)

    video = yt.streams.filter(only_audio=True).first()
    # download the audio
    video.download(path)


def download_video_from_youtube(link, path):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    # video = yt.streams.filter(progressive=True,file_extension='mp4')
    video.download(path)

f=[]
for i in urls:
    print(i)
    if answers["format"] == 'audio':
        try:
            download_audio_from_youtube(i, rf'{p}')
            print("audio downloaded")
        except:
            print("Failed to download audio")
            f.append(i)



    elif answers["format"] == 'video':
        print('dowanloading')
        try:
            download_video_from_youtube(i, rf'{p}')
            print("video downloaded")
        except:
            print("Failed to download video")
            f.append(i)
print(f)
save_path = p
file_name = "failed_urls.txt"

completeName = os.path.join(save_path, file_name)


F= open(completeName,'+w')
for i in f:
     F.write(f"{i} \n")

sys.exit()

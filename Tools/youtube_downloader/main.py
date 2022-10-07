import pytube

link = input('Enter youtube video URL:')
yt = pytube.YouTube(link)
yt.streams.first().download(output_path='videos/')
print('Downloaded', link)


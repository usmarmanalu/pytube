from pytube import YouTube

link = input("url youtube : ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))
for i in video:
    print(i)
    
print("pengaturan pemutaran video : ")
dnoption = int(input("format video : "))
dnvideo = videos[dnoption]
dnvideo.download()

print("dwonload sukses")

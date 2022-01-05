from pytube import YouTube


link = input("masukkan url youtube : ")
yt = YouTube("https://www.youtube.com/watch?v=0aybzPCAKp0")
videos = yt.streams.all()

video = list(enumerate(videos))
for i in video:
    print(i)
    
    
print("enter the desired option to dwonload format : ")
dnoption = int(input("enter the option : "))
dnvideo = videos[dnoption]
dnvideo.download()

print("dwonload sukses")

from pytube import YouTube


link = input("masukkan url youtube : ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))
for i in video:
    print(i)
    
    
print("enter the desired option to dwonload format : ")
dnoption = int(input("enter the option : "))
dnoption = videos[dnoption]
dnoption.download()

print("dwonload sukses")

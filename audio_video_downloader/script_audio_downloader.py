from pytube import YouTube

index = 1
links_txt = open("links.txt", "r")

for line in links_txt:
    line = line.replace("\n", "")

    youtube_link = line
    y = YouTube(youtube_link)
    t = y.streams.filter(only_audio=True)
    t[1].download(output_path="/downloads/")

    print('{} - Download de {} concluído com sucesso.'.format(index, line))
    index += 1

print("*** Todos os downloads foram finalizados ***")
links_txt.close()

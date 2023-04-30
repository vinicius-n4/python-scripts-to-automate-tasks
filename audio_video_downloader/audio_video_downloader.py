from pytube import YouTube
from tkinter import *


class Functions:
    def download_audio(self):
        video_object = YouTube(self.entry_link.get())
        audio_list = video_object.streams.filter(only_audio=True)
        audio_list[1].download(output_path='downloads')

    def download_video(self):
        video_object = YouTube(self.entry_link.get())
        to_download = video_object.streams.first()
        to_download.download(output_path='downloads')


class Application(Functions):
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.widgets_da_tela()
        self.root.mainloop()

    def tela(self):
        self.root.title('YT Audio Downloader')
        self.root.configure(background='#590000')
        self.root.geometry('500x300')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=300)

    def widgets_da_tela(self):
        self.lb_link = Label(self.root, text='Link:', bg='#590000', fg='white', font=('arial', 10, 'bold'))
        self.lb_link.place(relx=0.05, rely=0.1)
        self.entry_link = Entry(self.root)
        self.entry_link.place(relx=0.05, rely=0.18, relwidth=0.9)

        self.bt_download_audio = Button(self.root, text='Download Audio', bd=2, bg='white', font=('arial', 12, 'bold'),
                                  command=self.download_audio)
        self.bt_download_audio.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

        self.bt_download_video = Button(self.root, text='Download Video', bd=2, bg='white', font=('arial', 12, 'bold'),
                                        command=self.download_video)
        self.bt_download_video.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1)

Application()

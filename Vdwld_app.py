from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil


def download():
    vid_path = url_entry.get()
    file_path = path.cget("text")
    print('Downloading.......')
    mp4 = YouTube(vid_path).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4)
    
    audio_f = vid_clip.audio
    audio_f.write_audiofile('audio.mp3')
    audio_f.close()
    shutil.move('audio.mp3', file_path)

    
    
    vid_clip.close()
    shutil.move(mp4, file_path)
    print('Download Complete')
    
    

def get_path():
    path1 = filedialog.askdirectory()
    path.config(text=path1)

root = Tk()
root.title('Vedio Downloader')
canvas = Canvas(root, width=400, height=300)
canvas.pack()

app_label = Label(root, text="Vedio Downloader", fg='blue', font=('Ariel', 20))
canvas.create_window(200,20,window=app_label)

url_label = Label(root,text="Enter vedio URl")
url_entry = Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)


path = Label(root,text="Select path to download")
path_button = Button(root,text="Select",command=get_path)
canvas.create_window(200,150,window=path)
canvas.create_window(200,180,window=path_button)

dwld_button = Button(root,text='Download', command=download)
canvas.create_window(200,250,window=dwld_button)



root.mainloop()
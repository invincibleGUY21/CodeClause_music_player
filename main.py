import tkinter as tk
import fnmatch
import os
from pygame import mixer
from PIL import ImageTk, Image

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("1200x1200")
canvas.config(bg = "black")

rootpath = "C:\\Users\Om\Music\Bollywood"
pattern = "*.mp3"

mixer.init()

def picture(p):
    #Opening image
    image = Image.open(p)

    #Resizing image
    image = image.resize((50, 50), Image.ANTIALIAS)

    return image

str = "C:\\Users\\Om\\Documents\\Internships\\Code Clause\\Music Player in Python\\"

prev_img = ImageTk.PhotoImage(picture(str + "Previous.png"))
stop_img = ImageTk.PhotoImage(picture(str + "Stop.png"))
play_img = ImageTk.PhotoImage(picture(str + "Play.png"))
pause_img = ImageTk.PhotoImage(picture(str + "Pause.png"))
next_img = ImageTk.PhotoImage(picture(str + "Next.png"))

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()

    if next_song[0] != listBox.size() - 1:
        next_song = next_song[0] + 1

    else:
        next_song = 0

    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()

    if next_song[0] != 0:
        next_song = next_song[0] - 1

    else:
        next_song = 'end'

    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Resume"

    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

listBox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = "100", font = ('ds-digital', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font = ('ds-digital', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", command = play_prev, image = prev_img)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text = "Stop", command = stop, image = stop_img)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "Play", command = select, image = play_img)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause", command = pause_song, image = pause_img)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", command = play_next, image = next_img)
nextButton.pack(pady = 15, in_ = top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()

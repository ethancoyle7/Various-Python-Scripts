import tkinter as tk
from gtts import gTTS
import os

def speak():
    text = entry.get()
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")

root = tk.Tk()
root.title("Text to Speech")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Speak", command=speak)
button.pack()

root.mainloop()

import os
from tkinter import *
import random
from tkinter import messagebox as mb

try:
	from pygame import mixer
except:
	os.system('pip install pygame')
	from pygame import mixer

try:
	from gtts import gTTS
except:
	os.system('pip install gTTS')
	from gtts import gTTS
	
def speak():
	global word
	global ent
	word = random.choice(data).strip()
	text = gTTS(text=word, lang='en', slow = True)
	text.save("file.mp3")
	mixer.init()
	mixer.music.load('file.mp3')
	mixer.music.play()
	ent['text'] = ""
	

def check():
	inp = ent.get()
	if inp:
		try:
			if inp.lower()==word.lower():
				mb.showinfo("Spelling Checker", "Correct Spelling.")
			else:
				mb.showerror("Spelling Checker", "Incorrect Spelling!!\nCorrect Spelling is: {}".format(word.upper()))
		except NameError:
			mb.showerror("Spelling Checker", "No Word Given By Computer")
	else:
			mb.showwarning("Spelling Checker", "Enter Spelling")
	
f = open('words.txt', 'r')
data = f.readlines()


root = Tk()
root.geometry('900x650')
root.configure(bg='light blue')

Label(root, text = "Spelling Checker", font = ('Droid Sans Mono', 15), bg = 'light blue', fg = 'royalblue').pack(pady = 20)

btn_speak = Button(root, text = "Speak", bg = 'royalblue',command = speak, activebackground = 'royalblue', activeforeground = 'white', fg = 'white')
btn_speak.pack(pady = 20)

frm = LabelFrame(root, text = "Enter Spelling", bg = 'light blue')
frm.pack(pady = 20)

ent = Entry(frm)
ent.pack(padx = 20, pady = 20)

btn_check = Button(root, text = "Check Spelling", command = check, bg = 'royalblue', activebackground = 'royalblue', activeforeground = 'white', fg = 'white')
btn_check.pack(pady = 20)

root.mainloop()
import os
from tkinter import *
import random
from tkinter import messagebox as mb
# from time import sleep

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
	word = random.choice(data).strip()
	text = gTTS(text=word, lang='en', slow = True)
	for x in range(1000):
		fname = str(x)+'.mp3'
		if not os.path.exists(fname):
			text.save(fname)
			break
	else:
		pass
	mixer.init()
	mixer.music.load(fname)
	mixer.music.play()
	# sleep(1000)
	# mixer.music.unload()
	# os.remove(fname)
	

def check():
	inp = ent.get()
	try:
		if inp.lower()==word.lower():
			mb.showinfo("Spelling Checker", "Correct Spelling.")
		else:
			mb.showerror("Spelling Checker", "Incorrect Spelling!!\nCorrect Spelling is: {}".format(word.upper()))
	except NameError:
		mb.showerror("Spelling Checker", "No Word Given By Computer")
		

f = open('words.txt', 'r')
data = f.readlines()


root = Tk()
root.title("Spelling Checker Tool")
root.geometry('344x382')
root.configure(bg='light blue')

Label(root, text = "Spelling Checker", font = ('Droid Sans Mono', 15), bg = 'light blue', fg = 'royalblue').pack(pady = 20)

btn_speak = Button(root, text = "SPEAK", bg = 'royalblue',command = speak, activebackground = 'royalblue', activeforeground = 'white', fg = 'white')
btn_speak.pack(pady = 20)

frm = LabelFrame(root, text = "Enter Spelling", bg = 'light blue')
frm.pack(pady = 20)

ent = Entry(frm)
ent.pack(padx = 20, pady = 20)

btn_check = Button(root, text = "CHECK SPELLING", command = check, bg = 'royalblue', activebackground = 'royalblue', activeforeground = 'white', fg = 'white')
btn_check.pack(pady = 20)

root.mainloop()
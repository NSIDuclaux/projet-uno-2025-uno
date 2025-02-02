from tkinter import *
from PIL import Image, ImageTk
from pygame import *

#Musique de fond

mixer.init()
mixer.music.load("Main_Theme.mp3")
mixer.music.play(-1)

#Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")

#Fond

fond_image = Image.open("Fond.jpg")
fond_image = fond_image.resize((1620,840))
fond = ImageTk.PhotoImage(fond_image)

fond_label = Label(fenetre, image=fond)
fond_label.place(x=0, y=0, relwidth=1, relheight=1)

#Element Interface



fenetre.mainloop()
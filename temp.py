from os import path
from tkinter import *
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen",True)

frame_victoire = Frame(fenetre)
frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

frame_defaite = Frame(fenetre)
frame_victoire.place(relx=0.5, rely=0.5, anchor=CENTER,width=1600,height=800)

ratio = 0.2

image_victoire = Image.open(path.abspath("Interface/Victoire.png"))
new_size = (int(image_victoire.width * ratio), int(image_victoire.height * ratio))
image_victoire = image_victoire.resize(new_size)
image_victoire = ImageTk.PhotoImage(image_victoire)

image_defaite = Image.open(path.abspath("Interface/Defaite.png"))
image_defaite = image_defaite.resize(new_size)
image_defaite = ImageTk.PhotoImage(image_defaite)

label_victoire = Label(frame_victoire,image=image_victoire)
label_victoire.place(relx=0.5, rely=0.5, anchor=CENTER)
label_defaite = Label(frame_defaite,image=image_defaite)
label_defaite.place(relx=0.5, rely=0.5, anchor=CENTER)

fenetre.mainloop()

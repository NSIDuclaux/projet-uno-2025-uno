from tkinter import *
from PIL import Image, ImageTk
from os import path

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen")

fond = "#1e1e1e"
fenetre.config(bg=fond)

index_couleur = IntVar(value=-1)

# Fonction bouton

def afficher_index_couleur(valeur) :

    index_couleur.set(valeur)
    print("Index couleur :", index_couleur.get())

#Frame

frame_changer_couleur = Frame(fenetre, bg=fond)

#Creation Image

ratio = 0.2

fond_path = path.abspath("Interface/Changer de couleur/Interface.png")
fond_changer_couleur = Image.open(fond_path)
new_size = (int(fond_changer_couleur.width * ratio), int(fond_changer_couleur.height * ratio))
fond_changer_couleur = fond_changer_couleur.resize(new_size)
fond_changer_couleur = ImageTk.PhotoImage(fond_changer_couleur)


image_bleu = Image.open(path.abspath("Interface/Changer de couleur/Bleu.png"))

ratio = 0.2
new_size = (int(image_bleu.width * ratio), int(image_bleu.height * ratio))

image_bleu = image_bleu.resize(new_size)
image_bleu = ImageTk.PhotoImage(image_bleu)

image_cyan = Image.open(path.abspath("Interface/Changer de couleur/Cyan.png"))
image_cyan = image_cyan.resize(new_size)
image_cyan = ImageTk.PhotoImage(image_cyan)

image_rose = Image.open(path.abspath("Interface/Changer de couleur/Rose.png"))
image_rose = image_rose.resize(new_size)
image_rose = ImageTk.PhotoImage(image_rose)

image_violet = Image.open(path.abspath("Interface/Changer de couleur/Violet.png"))
image_violet = image_violet.resize(new_size)
image_violet = ImageTk.PhotoImage(image_violet)

#Label & Bouton

fond_label = Label(fenetre, image=fond_changer_couleur, bg=fond)
fond_label.place(anchor="center", relx=0.5, rely=0.5) 

bouton_bleu = Button(frame_changer_couleur, image=image_bleu, bg="#121212", command=lambda: afficher_index_couleur(0), borderwidth=0, activebackground="#121212").grid(row=0, column=0, padx=0)
bouton_cyan = Button(frame_changer_couleur, image=image_cyan, bg="#121212", command=lambda: afficher_index_couleur(1) ,borderwidth=0, activebackground="#121212").grid(row=0, column=1, padx=0)
bouton_rose = Button(frame_changer_couleur, image=image_rose, bg="#121212", command=lambda: afficher_index_couleur(2) ,borderwidth=0, activebackground="#121212").grid(row=0, column=2, padx=0)
bouton_violet = Button(frame_changer_couleur, image=image_violet, bg="#121212", command=lambda: afficher_index_couleur(3) ,borderwidth=0, activebackground="#121212").grid(row=0, column=3, padx=0)

frame_changer_couleur.place(anchor="center", relx=0.5, rely=0.5, y=30)
frame_changer_couleur.lift()

fenetre.mainloop()


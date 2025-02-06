from tkinter import *
from PIL import Image, ImageTk
#from pygame import mixer
from subprocess import run

#Fonction Bouton

def bouton_jouer():

    fenetre.destroy()
    run(["python", "interface_jeu.py"])

def bouton_jouer_entrer(event):

    bouton1_button.config(image=bouton1_image_large)

def bouton_jouer_sortie(event):

    bouton1_button.config(image=bouton1_image_normal)

def bouton_parametre():

    fenetre.destroy()
    run(["python", "interface_paramètre.py"])

def bouton_parametre_entrer(event):

    bouton2_button.config(image=bouton2_image_large)

def bouton_parametre_sortie(event):

    bouton2_button.config(image=bouton2_image_normal)

def bouton_quitter():

    fenetre.destroy()

def bouton_quitter_entrer(event):

    bouton3_button.config(image=bouton3_image_large)

def bouton_quitter_sortie(event):

    bouton3_button.config(image=bouton3_image_normal)



#Musique de fond

# mixer.init()
# mixer.music.load("Main_Theme.mp3")
# mixer.music.play(-1)

#Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen",True)

#Fond

fond = "#1e1e1e"
fenetre.config(bg=fond)

#Element Interface

logo_image = Image.open("Logo.png").resize((450, 450))
logo_image = ImageTk.PhotoImage(logo_image)

logo_label = Label(fenetre, image=logo_image, bg="#1e1e1e")
logo_label.place(relx=0.5, rely=0.25, anchor='center')

bouton1_image_normal = Image.open("Bouton Jouer.png").resize((400,130 ))
bouton1_image_normal = ImageTk.PhotoImage(bouton1_image_normal)

bouton1_image_large = Image.open("Bouton Jouer.png").resize((480,156 ))
bouton1_image_large = ImageTk.PhotoImage(bouton1_image_large)

bouton1_button = Button(fenetre, image=bouton1_image_normal, bg="#1e1e1e", width=500, height=100,command=bouton_jouer,borderwidth=0,activebackground="#1e1e1e")
bouton1_button.place(relx=0.5, rely=0.6, anchor='center')

bouton2_image_normal = Image.open("Bouton Paramètre.png").resize((400,130 ))
bouton2_image_normal = ImageTk.PhotoImage(bouton2_image_normal)

bouton2_image_large = Image.open("Bouton Paramètre.png").resize((480,156 ))
bouton2_image_large = ImageTk.PhotoImage(bouton2_image_large)

bouton2_button = Button(fenetre, image=bouton2_image_normal, bg="#1e1e1e", width=500, height=100,command=bouton_parametre,borderwidth=0,activebackground="#1e1e1e")
bouton2_button.place(relx=0.5, rely=0.72, anchor='center')

bouton3_image_normal = Image.open("Bouton Quitter.png").resize((400,130 ))
bouton3_image_normal = ImageTk.PhotoImage(bouton3_image_normal)

bouton3_image_large = Image.open("Bouton Quitter.png").resize((480,156 ))
bouton3_image_large = ImageTk.PhotoImage(bouton3_image_large)

bouton3_button = Button(fenetre, image=bouton3_image_normal, bg="#1e1e1e", width=500, height=100,command=bouton_quitter,borderwidth=0,activebackground="#1e1e1e")
bouton3_button.place(relx=0.5, rely=0.84, anchor='center')

#Interaction avec la page

bouton1_button.bind("<Enter>", bouton_jouer_entrer)
bouton1_button.bind("<Leave>", bouton_jouer_sortie)

bouton2_button.bind("<Enter>", bouton_parametre_entrer)
bouton2_button.bind("<Leave>", bouton_parametre_sortie)

bouton3_button.bind("<Enter>", bouton_quitter_entrer)
bouton3_button.bind("<Leave>", bouton_quitter_sortie)

fenetre.mainloop()
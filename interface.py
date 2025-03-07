from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from os import *
from interface_jeu_POO import *

#Frame

def affiché_frame_menu(partie):
    
    if partie:
        partie.destroy()
    
    frame_menu.pack(fill="both", expand=True)

def bouton_rejouer(partie,frame):

    print("Rejouer")

    if partie:
        partie_en_cours.destroy()
    partie_en_cours = PartieJeu(frame)
    partie_en_cours.pack(fill="both", expand=True)


def affiché_frame_jeu():

    frame_menu.pack_forget()
    


#Fonction Bouton

partie_en_cours = None

def bouton_jouer():

    global fenetre
    global partie_en_cours
    affiché_frame_jeu()

    if partie_en_cours is None:
        partie_en_cours = PartieJeu(fenetre)  #  Ajoute l'interface dans `frame_jeu
        partie_en_cours.pack(fill="both", expand=True)

def bouton_jouer_entrer(event):

    bouton1_button.config(image=bouton1_image_large)

def bouton_jouer_sortie(event):

    bouton1_button.config(image=bouton1_image_normal)
def bouton_quitter():

    fenetre.destroy()

def bouton_quitter_entrer(event):

    bouton3_button.config(image=bouton3_image_large)

def bouton_quitter_sortie(event):

    bouton3_button.config(image=bouton3_image_normal)



#Musique de fond

main_theme_path = path.abspath("Interface/Son/Main_Theme.mp3")

mixer.init()
mixer.music.load(main_theme_path)
mixer.music.play(-1)

#Création de la fenêtre

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen",True)

#Fond

fond = "#1e1e1e"
fenetre.config(bg=fond)

##Frame

frame_menu = Frame(fenetre,bg=fond)
frame_jeu = Frame(fenetre,bg=fond)

#Frame_menu

logo_path = path.abspath("Interface/Logo.png")
logo_image = Image.open(logo_path).resize((450, 450))
logo_image = ImageTk.PhotoImage(logo_image)

logo_label = Label(frame_menu, image=logo_image, bg="#1e1e1e")
logo_label.place(relx=0.5, rely=0.25, anchor='center')

bouton1_path = path.abspath("Interface/Bouton/Bouton Jouer.png")
bouton1_image_normal = Image.open(bouton1_path).resize((400,130 ))
bouton1_image_normal = ImageTk.PhotoImage(bouton1_image_normal)

bouton1_image_large = Image.open(bouton1_path).resize((480,156 ))
bouton1_image_large = ImageTk.PhotoImage(bouton1_image_large)

bouton1_button = Button(frame_menu, image=bouton1_image_normal, bg="#1e1e1e", width=500, height=100,command=bouton_jouer,borderwidth=0,activebackground="#1e1e1e")
bouton1_button.place(relx=0.5, rely=0.7, anchor='center')


bouton3_path = path.abspath("Interface/Bouton/Bouton Quitter.png")
bouton3_image_normal = Image.open(bouton3_path).resize((400,130 ))
bouton3_image_normal = ImageTk.PhotoImage(bouton3_image_normal)

bouton3_image_large = Image.open(bouton3_path).resize((480,156 ))
bouton3_image_large = ImageTk.PhotoImage(bouton3_image_large)

bouton3_button = Button(frame_menu, image=bouton3_image_normal, bg="#1e1e1e", width=500, height=100,command=bouton_quitter,borderwidth=0,activebackground="#1e1e1e")
bouton3_button.place(relx=0.5, rely=0.82, anchor='center')

#Frame Jeu


#Interaction avec la page

#Menu

bouton1_button.bind("<Enter>", bouton_jouer_entrer)
bouton1_button.bind("<Leave>", bouton_jouer_sortie)

bouton3_button.bind("<Enter>", bouton_quitter_entrer)
bouton3_button.bind("<Leave>", bouton_quitter_sortie)

#Ne pas touché

frame_menu.pack(fill="both", expand=True)

fenetre.mainloop()
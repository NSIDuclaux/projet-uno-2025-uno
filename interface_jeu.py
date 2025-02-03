from tkinter import *

fenetre = Tk()
fenetre.title("Cosmunos")
fenetre.geometry("1600x800")
fenetre.attributes("-fullscreen",True)

label = Label(fenetre, text="Teste")
label.pack()

fond = "#1e1e1e"
fenetre.config(bg=fond)

fenetre.mainloop()
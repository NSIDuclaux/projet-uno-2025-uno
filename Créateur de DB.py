import sqlite3

# Connexion
connexion = sqlite3.connect('base_de_donnees.db')

# Récupération d'un curseur
c = connexion.cursor()

# ---- Début des instructions SQL

# Création de la table
c.execute("""
    CREATE TABLE IF NOT EXISTS carte(
    IDCouleur INT,
    IDCarte INT,
    Chemin TEXT);
""")

# Insertion des données
for i in range(4):  # Boucle pour les couleurs (0,1,2)
    for k in range(15):  # Boucle pour les cartes (0 à 13)
        c.execute("INSERT INTO carte (IDCouleur, IDCarte, Chemin) VALUES (?, ?, ?)", (i, k, "carte/couleur/.png"))

# Validation
connexion.commit()

# Déconnexion
connexion.close()
# Cosmunos

**Cosmunos** est un jeu de UNO spatial mêlant stratégie et hasard, réalisé dans le cadre d'un projet de NSI. Ce projet propose une version console ainsi qu'une interface graphique immersive inspirée du thème de l'espace.

## Prérequis

Pour exécuter ce projet, vous devez disposer des éléments suivants :

- **Python 3.11** ou une version supérieure
- Bibliothèques Python suivantes (installables via pip) :
  - `tkinter` (intégré dans Python par défaut)
  - `sqlite3` (intégré dans Python par défaut)
  - `os`(intégé dans Python par défaut)
  - `pygame` (bibliothèque à installer)
  - `pillow` (bibliothèque à installer)

## Installation

1. Programme disponible dans  :
   ```bash
   git clone <URL_DU_DEPOT>
   cd Cosmunos
   ```

2. Assurez-vous d'avoir la version correcte de Python :
    ```bash
    --python --version
    ```

3. Lancez le jeu :

   - **Version console :**
     ```bash
     python main_console.py
     ```
   
   - **Version graphique :**
     ```bash
     python main_interface.py
     ```

## Fonctionnalités

- Jeu de UNO avec règles standards et variantes personnalisées
- Interface graphique thématisée sur l'espace
- Intelligence artificielle (bot) capable de jouer
- Gestion de la pioche et des cartes en temps réel

## Équipe du projet

Le projet a été réalisé par :
- **Estaban MOLINA** : Développement des classes primitives
- **Nicolas MOURADOFF** : Fusion des classes et création de la classe `bot`
- **Quentin CHAMBRE-LAVERGNE** : Interface graphique et adaptation du code pour l'interface

## Outils utilisés

- **Visual Studio Code** pour le développement
- **GitHub** pour le partage de fichiers et la gestion de version
- **Discord** pour la communication entre les membres
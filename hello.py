from pathlib import Path
import os

# Recuperer le chemin du Bureau Windows
desktop = Path(os.environ["USERPROFILE"]) / "Desktop"

# Definir le fichier de sortie
inventaire = Path(os.environ["TEMP"]) / "inventaire.txt"

# Recuperer les noms des fichiers et dossiers
elements = list(desktop.iterdir())

# Creer le fichier texte
with open(inventaire, "w", encoding="utf-8") as fichier:
    fichier.write("INVENTAIRE DU BUREAU\n")
    fichier.write("====================\n\n")

    for element in elements:
        fichier.write(element.name + "\n")

print("Inventaire cree avec succes !")
print("Emplacement :", inventaire)
print("Nombre d'elements :", len(elements))

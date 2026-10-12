from pathlib import Path
import os
import subprocess

# 1. Localiser le Bureau Windows
desktop = Path.home() / "Desktop"

# 2. Creer le dossier du TP
dossier = Path(os.environ["TEMP"]) / "FlipperTP"
dossier.mkdir(parents=True, exist_ok=True)

# 3. Creer le fichier inventaire.txt
inventaire = dossier / "inventaire.txt"

with inventaire.open("w", encoding="utf-8") as f:
    f.write("INVENTAIRE DU BUREAU\n")
    f.write("===================\n\n")

    for element in sorted(desktop.iterdir()):
        f.write(element.name + "\n")

print("Inventaire cree :", inventaire)

# 4. Preparer un email avec Outlook
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)

# Adresse du destinataire
mail.To = "ami@example.com"

mail.Subject = "TP Flipper Zero - Inventaire"
mail.Body = "Bonjour, voici mon fichier inventaire."

# 5. Ajouter automatiquement la piece jointe
mail.Attachments.Add(str(inventaire))

# 6. Ouvrir le message pour verification et envoi
mail.Display()

print("Email prepare avec la piece jointe.")

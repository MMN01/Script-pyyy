
import smtplib
import os
from pathlib import Path
from email.message import EmailMessage

# Configuration Gmail
expediteur = "damirzizo4@gmail.com"
destinataire = "mnyahya007@gmail.com"

# Mot de passe d'application Gmail
mot_de_passe = input("entre ton password")

# Creer un fichier de test
fichier = Path(os.environ["TEMP"]) / "test_flipper.txt"
fichier.write_text("Hello amigo !", encoding="utf-8")

# Preparer le message
mail = EmailMessage()
mail["From"] = expediteur
mail["To"] = destinataire
mail["Subject"] = "TP Flipper Zero"
mail.set_content("Voici mon fichier de test.")

# Ajouter la piece jointe
mail.add_attachment(
    fichier.read_bytes(),
    maintype="text",
    subtype="plain",
    filename=fichier.name
)

# Envoyer automatiquement
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(expediteur, mot_de_passe)
    smtp.send_message(mail)

print("Email envoye avec succes !")

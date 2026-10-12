from pathlib import Path
from email.message import EmailMessage
import ctypes
import getpass
import os
import smtplib

# =====================================
# 1. CONFIGURATION
# =====================================

expediteur = input("Ton adresse Gmail : ").strip()
destinataire = input("Adresse de ton ami : ").strip()

# =====================================
# 2. LOCALISER LE BUREAU WINDOWS
# =====================================

# Compatible avec les Bureaux rediriges
# notamment vers OneDrive

buffer = ctypes.create_unicode_buffer(260)

ctypes.windll.shell32.SHGetFolderPathW(
    None, 0, None, 0, buffer
)

desktop = Path(buffer.value)

# =====================================
# 3. CREER LE FICHIER TXT
# =====================================

dossier = Path(os.environ["TEMP"]) / "FlipperTP"
dossier.mkdir(parents=True, exist_ok=True)

inventaire = dossier / "inventaire.txt"

elements = sorted(
    element.name for element in desktop.iterdir()
)

with inventaire.open("w", encoding="utf-8") as f:
    f.write("INVENTAIRE DU BUREAU\n")
    f.write("===================\n\n")

    for nom in elements:
        f.write(nom + "\n")

print("Fichier cree :", inventaire)
print("Nombre d'elements :", len(elements))

# =====================================
# 4. PREPARER LE MAIL
# =====================================

message = EmailMessage()

message["From"] = expediteur
message["To"] = destinataire
message["Subject"] = "TP Flipper Zero - Inventaire"

message.set_content(
    "Bonjour,\n\n"
    "Voici le fichier inventaire.txt "
    "en piece jointe.\n\n"
    "Bonne reception."
)

# Ajouter la piece jointe
message.add_attachment(
    inventaire.read_bytes(),
    maintype="text",
    subtype="plain",
    filename=inventaire.name
)

# =====================================
# 5. VERIFICATION ET ENVOI
# =====================================

print("\nContenu du fichier :\n")
print(inventaire.read_text(encoding="utf-8"))

print("\nDestinataire :", destinataire)

confirmation = input(
    "\nAutoriser l'envoi de cet inventaire ? (oui/non) : "
)

if confirmation.strip().lower() == "oui":

    mot_de_passe = getpass.getpass(
        "Mot de passe d'application Gmail : "
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com", 465, timeout=30
    ) as smtp:

        smtp.login(expediteur, mot_de_passe)
        smtp.send_message(message)

    print("\nEmail envoye avec succes !")

else:
    print("\nEnvoi annule.")

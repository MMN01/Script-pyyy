import socket

HOST = "0.0.0.0"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    serveur.bind((HOST, PORT))
    serveur.listen(1)

    print("Serveur demarre.")
    print("En attente d'une connexion...")

    connexion, adresse = serveur.accept()

    with connexion:
        print("Client connecte :", adresse)

        while True:
            message = connexion.recv(1024)

            if not message:
                break

            texte = message.decode("utf-8")
            print("Message recu :", texte)

            if texte.lower() == "quit":
                break

            reponse = input("Reponse : ")
            connexion.sendall(reponse.encode("utf-8"))

print("Connexion terminee.")

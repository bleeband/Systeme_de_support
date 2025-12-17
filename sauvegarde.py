#système de sauvegarde

def sauvegarde_ticket(numero_ticket, probleme, nom, prenom, email, priorite):
    # on ouvre un fichier, si inexistant ça le crée au format numero_de_ticket.json
    file = open(f"{numero_ticket}.json", 'w')
    # on inscrit l'info dans le .json
    file.write(f"Numero: {numero_ticket}\nProbleme: {probleme}\nNom: {nom}\nPrenom: {prenom}\nEmail: {email}\nPriorite: {priorite}\n")
    # on ferme le fichier
    file.close()

# #-----test - doit créer un ticket appellé 4124.json dans le dossier tickets
# numero_ticket = 4124
# probleme = "Ca ne marche pas"
# nom = "Gosselin"
# prenom = "Mathieu"
# email = "math@email.com"
# priorite = 1
# sauvegarde_ticket(numero_ticket, probleme, nom, prenom, email, priorite)


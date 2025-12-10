#système de sauvegardes

def sauvegarde_ticket(numero_ticket, probleme, nom, email):
    file = open(f"{numero_ticket}.json", 'w')
    file.write(f"Numero:{numero_ticket}\nProbleme:{probleme}\nNom:{nom}\nEmail:{email}\n")
    file.close()

##-----test - doit créer un ticket appellé 4124.json dans le dossier tickets
# numero_ticket = 4124
# probleme = "Ca ne marche pas"
# nom = "Mathieu"
# email = "math@email.com"
# sauvegarde_ticket(numero_ticket, probleme, nom, email)


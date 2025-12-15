import interface
import ticket
import sauvegarde

while True:
    choix = interface.menu() 

    if choix == "4":
        sauvegarde.sauvegarde_ticket()

    elif choix == "5":
        print("Au revoir !")
        break

    else:
        print("Choix invalide, recommencez svp")
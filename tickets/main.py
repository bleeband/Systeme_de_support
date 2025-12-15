import gestion
import interface
import ticket
import sauvegarde

while True:
    choix = int(interface.menu())
    
    if choix == 1:
    
        prenom, nom, courriel, probleme, _ = ticket.collecter_info_ticket()
        nom_complet = prenom + " " + nom
        print(nom_complet)    
        gestion.creer_ticket(probleme, nom_complet, courriel)
        
    elif interface.menu() == "2":
        print("Afficher la liste des tickets.\n")
        gestion.afficher_tickets()
    
    elif interface.menu() == "3":
        print("Modification de ticket.\n")
        gestion.update_ticket(num_ticket, info_a_changer, changement)

    elif choix == "4":
        gestion.supprimer_ticket(num_ticket)

    elif choix == "5":
        print("Au revoir !")
        for ticket in gestion.tickets:
            sauvegarde.sauvegarde_ticket(["numero"], ["probleme"], ["nom"], ["email"])
        break

    else:
        print("Choix invalide, recommencez svp")
        



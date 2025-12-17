import gestion
import interface
import ticket
import sauvegarde

while True:
    choix = interface.menu()
    
    if choix == "1":
        prenom, nom, email, probleme, priorite = ticket.collecter_info_ticket()   
        gestion.creer_ticket(probleme, nom, prenom, email, priorite)
        
    elif choix == "2":
        print("\n--- Afficher la liste des tickets ---\n")
        gestion.afficher_tickets()
    
    elif choix == "3":
            print("\n--- Modification de ticket ---\n")
            numero_ticket = int(input("Entrer le numero de ticket : "))
            info_a_changer = input("Entrer une nouvelle description : ")
            gestion.update_ticket(numero_ticket, info_a_changer)

    elif choix == "4":
        print("\n--- Suppression du ticket ---\n")
        try:
            numero_ticket = int(input("Entrer le numero de ticket : "))
            if gestion.supprimer_ticket(numero_ticket):
                print(f"Ticket supprimé  avec succès !")
            else:
                print("\nTicket introuvable")
        except ValueError:
            print("\nChoix invalide, entrer un nombre")

    elif choix == "5":
        print("\nAu revoir !")
        for ticket_item in gestion.tickets:
            sauvegarde.sauvegarde_ticket(ticket_item["numero"], ticket_item["probleme"], ticket_item["nom"], ticket_item["prenom"], ticket_item["email"], ticket_item["priorite"])
        break

    else:
        print("\nChoix invalide, veuillez recommencer s.v.p")
        



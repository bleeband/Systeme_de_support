import gestion
import interface
import ticket

while True:

    choix = int(interface.menu())


    if choix == 1:
    
        prenom, nom, courriel, probleme, _ = ticket.collecter_info_ticket()
        nom_complet = prenom + " " + nom
        print(nom_complet)    
        gestion.creer_ticket(probleme, nom_complet, courriel)
        
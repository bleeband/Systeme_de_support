import sauvegarde
import interface
import gestion

elif interface.menu() == "2":
    print("Afficher la liste des tickets.\n")
    gestion.afficher_tickets()


for ticket in gestion.tickets:
    sauvegarde.sauvegarde_ticket(["numero"], ["probleme"], ["nom"], ["email"])
import interface
import gestion



for ticket in gestion.tickets:
    if interface.menu == "3":
        print("Modification de ticket.\n")
        gestion.update_ticket()




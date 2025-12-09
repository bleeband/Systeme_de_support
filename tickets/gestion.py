tickets = []
numero_ticket = 1

def creer_ticket(probleme, nom, email):
    global numero_ticket

    tickets.append({'numero': numero_ticket, 'probleme': probleme, 'nom': nom, "email": email})
    numero_ticket +=1
    print(f"Ticket créé !")

def afficher_tickets():

    print(tickets)

def update_ticket(num_ticket, info_a_changer, changement):

    for ticket in tickets:
        if ticket['numero'] == num_ticket:
            ticket[info_a_changer] = changement
            print(f"Changement effectué !")
            break
            

def supprimer_ticket(num_ticket):

    for ticket in tickets:
        if ticket['numero'] == num_ticket:
            tickets.remove(ticket)
            print(f"Ticket supprimé !")
            break

creer_ticket("Bug", "Clement", "clement_laflamme@videotron.ca")
afficher_tickets()
update_ticket(1, "probleme", "Bug grave")
afficher_tickets()
supprimer_ticket(1)
afficher_tickets()
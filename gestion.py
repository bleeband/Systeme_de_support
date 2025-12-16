tickets = [
    {"numero": 0,"nom": "dufour", "prenom": "marc", "email": "aa@bb.cc", "probleme": "Blue screen", "priorite": "faible" },
]
numero_ticket = 1

def creer_ticket(probleme, nom, prenom, email, priorite):
    global numero_ticket

    tickets.append({'numero': numero_ticket, 'probleme': probleme, 'nom': nom, 'prenom': prenom, "email": email, "priorite": priorite})
    numero_ticket +=1
    print(f"Ticket créé !")

def afficher_tickets():
    for ticket in tickets:
        print(f"Ticket # {ticket['numero']} - {ticket['priorite']} - {ticket['probleme']} demandé par {ticket['prenom']} {ticket['nom']} ({ticket['email']})")

def update_ticket(numero_ticket, info_a_changer):

    for ticket in tickets:
        if ticket['numero'] == numero_ticket:
            ticket['probleme'] = info_a_changer
            print(f"Changement effectué !")
            break         

def supprimer_ticket(numero_ticket):

    for ticket in tickets:
        if ticket['numero'] == numero_ticket:
            tickets.remove(ticket)
            numero_ticket -=1
            print(f"Ticket supprimé !")
            break

# creer_ticket("Bug", "Clement", "clement_laflamme@videotron.ca")
# afficher_tickets()
# update_ticket(1, "probleme", "Bug grave")
# afficher_tickets()
# supprimer_ticket(1)
# afficher_tickets()
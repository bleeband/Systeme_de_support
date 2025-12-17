tickets = [
    {"numero": 0,"nom": "Dufour", "prenom": "Marc", "email": "aa@bb.con", "probleme": "Code 18", "priorite": "faible" },
]
numero_ticket = 1

def creer_ticket(probleme, nom, prenom, email, priorite):
    global numero_ticket

    tickets.append({'numero': numero_ticket, 'probleme': probleme, 'nom': nom, 'prenom': prenom, "email": email, "priorite": priorite})
    numero_ticket +=1

def afficher_tickets():
    for ticket in tickets:
        print(f"Ticket # {ticket['numero']} • {ticket['priorite'].capitalize()} • {ticket['probleme']}; demandé par {ticket['prenom'].title()} {ticket['nom'].title()} ({ticket['email']})")

def update_ticket(numero_ticket, info_a_changer):

    for ticket in tickets:
        if ticket['numero'] == numero_ticket:
            ticket['probleme'] = info_a_changer
            print(f"\nChangement effectué  avec succès !")
            break         

def supprimer_ticket(numero_ticket):

    for ticket in tickets:
        if ticket['numero'] == numero_ticket:
            tickets.remove(ticket)
            numero_ticket -=1

            break

# creer_ticket("Bug", "Clement", "clement_laflamme@videotron.ca")
# afficher_tickets()
# update_ticket(1, "probleme", "Bug grave")
# afficher_tickets()
# supprimer_ticket(1)
# afficher_tickets()
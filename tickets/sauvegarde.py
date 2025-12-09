#système de sauvegardes

def sauvegarde_ticket(numero, ticket, nom, email, priorite):
    file = open(f"{nom}.json", 'w')
    file.write(f"Probleme:{ticket}\nNom:{nom}\nNumero:{numero}\nEmail:{email}\nPriorité:{priorite}")
    file.close()

# #test
# sauvegarde_ticket(4125, "Ca ne marche pas", "Mathieu", "math@email.com", 1)


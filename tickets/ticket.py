# Creation du tickets

def collecter_info_ticket():
    print("=== Création d'un ticket ===\n")
    
    # Collecte des informations
    prenom = input("Veuillez entrer votre prénom : ")
    nom = input("Veuillez entrer votre nom : ")
    courriel = input("Veuillez entrer votre courriel : ")
    description = input("Entrer une description du problème : ")

    # Sélection de la priorité
    print("Priorité : ")
    print("1 - Faible")
    print("2 - Moyenne")
    print("3 - Haute")

    choix = input("Entrer votre choix 1, 2, 3 : ")

    if choix == "1":
        priorite = "faible"
    elif choix == "2":
        priorite = "moyenne"
    elif choix == "3":
        priorite = "haute"
    else:
        print(input("Veuillez faire un choix entre 1, 2, 3 : "))
        priorite = "faible"
    print(f"Merci, votre ticket numéro #var_a_definir à été créé.  Un suivi vous sera fait sous 48 hrs\n")
    print(f"{prenom} {nom} {courriel} : {description} --> {priorite}\n")
    print("=== TERMINER ===")

    return prenom, nom, courriel, description, priorite
    
collecter_info_ticket()
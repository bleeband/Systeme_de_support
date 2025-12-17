# Creation du tickets

def collecter_info_ticket():
    print("\n--- Création d'un nouveau ticket ---\n")
    
    # Collecte des informations
    prenom = input("Veuillez entrer votre prénom : ")
    nom = input("Veuillez entrer votre nom : ")
    email = input("Veuillez entrer votre courriel : ")
    probleme = input("Entrer une description du problème : ")
    
    # Sélection de la priorité
    print("\nPriorité : ")
    print("1 - Faible")
    print("2 - Moyenne")
    print("3 - Haute")

    choix = input("\nEntrer faire votre choix : ")

    if choix == "1":
        priorite = "faible"
    elif choix == "2":
        priorite = "moyenne"
    elif choix == "3":
        priorite = "haute"
    else:
        print(input("Veuillez faire un choix entre : "))
        priorite = "faible"

    print(f"\nMerci {prenom.title()} {nom.title()}, votre ticket à été créé. Un suivi via {email} vous sera fait sous 48 hrs\n")

    return prenom, nom, email, probleme, priorite

# TEST
# collecter_info_ticket()
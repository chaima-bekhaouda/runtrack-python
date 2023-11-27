def supprimer_doublons(liste):
    # Créer une liste vide pour stocker les éléments uniques
    liste_sans_doublons = []

    # Parcourir chaque élément dans la liste initiale
    for element in liste:
        # Vérifier si l'élément n'est pas déjà présent dans la liste sans doublons
        if element not in liste_sans_doublons:
            # Ajouter l'élément à la liste sans doublons
            liste_sans_doublons.append(element)

    # Renvoyer la liste sans doublons
    return liste_sans_doublons

# Liste initiale
liste_initiale = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appeler la fonction pour supprimer les doublons
liste_sans_doublons = supprimer_doublons(liste_initiale)

# Afficher les résultats
print(liste_initiale)
print(liste_sans_doublons)
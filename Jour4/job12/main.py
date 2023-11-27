def tri_insertion(liste):
    # Parcourir la liste à partir du deuxième élément (indice 1)
    for i in range(1, len(liste)):
        # Stocker la valeur actuelle pour comparaison
        valeur_courante = liste[i]
        # Stocker la position actuelle dans la liste
        position = i

        # Déplacer les éléments plus grands vers la droite
        # jusqu'à ce que la bonne position pour la valeur_courante soit trouvée
        while position > 0 and liste[position - 1] > valeur_courante:
            liste[position] = liste[position - 1]
            position -= 1

        # Insérer la valeur_courante à la position correcte
        liste[position] = valeur_courante

# Première liste
liste1 = [392, 1092, 29, 4509, 898, 88]

# Appeler la fonction de tri par insertion
tri_insertion(liste1)

# Afficher la première liste triée
print(liste1)

# Deuxième liste
liste2 = [209, 59, 910, 4320, 903, 4]

# Appeler la fonction de tri par insertion
tri_insertion(liste2)

# Afficher la deuxième liste triée
print(liste2)
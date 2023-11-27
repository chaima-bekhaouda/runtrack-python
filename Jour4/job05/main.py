# Création d'une liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Affichage de la liste initiale
print(L)

# Affichage de la deuxième valeur de la liste
print(L[1])

# Définition de la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
def remplacer_et_afficher():
    L[3] = L[2] + L[4]
    print(L)

# Appel de la fonction pour effectuer le remplacement
remplacer_et_afficher()

# Affichage de la dernière valeur de la liste
print(L[-1])

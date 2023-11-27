# Définition de la liste L
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation du produit
produit = 1

# Calcul du produit des valeurs comprises dans l'intervalle [25, 90]
for nombre in L:
    if 25 <= nombre <= 90:
        produit *= nombre

# Affichage du résultat
print(produit)

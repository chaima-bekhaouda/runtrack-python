# Définition de la liste L
L = [8, 24, 48, 2, 16]

# Initialisation du compteur
nombre_de_multiples_de_3 = 0

# Parcours de la liste et comptage des multiples de 3
for nombre in L:
    if nombre % 3 == 0:
        nombre_de_multiples_de_3 += 1

# Affichage du résultat
print("Nombre de multiples de 3 dans la liste:", nombre_de_multiples_de_3)
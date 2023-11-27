# Définition de la liste L
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialisation de la somme
somme_des_paires = 0

# Parcours de la liste et calcul de la somme des valeurs paires
for nombre in L:
    if nombre % 2 == 0:
        somme_des_paires += nombre

# Affichage du résultat
print("Somme des valeurs paires dans la liste:", somme_des_paires)
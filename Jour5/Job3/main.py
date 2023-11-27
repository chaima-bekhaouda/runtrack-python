def triangle(height):
    if height <= 0:
        raise ValueError("Hauteur invalide: La hauteur doit être supérieure à 0")
    
    l_diag = "/"  # Caractères pour côtés du triangle
    r_diag = "\\"  # Il y a deux backslashes car '\' est un caractère spécial

    # Pour calculer la marge avant de dessiner
    empty_side = height - 1
    # Pour calculer l'espace à l'intérieur du triangle
    empty_mid = height * 2 - empty_side * 2 - 2

    # Boucle permettant de dessiner le triangle
    for i in range(height):
        # Insérer du vide à côté et à l'intérieur du triangle
        empty_char = " " * empty_side
        empty_char_mid = " " * empty_mid

        # Si on a atteint la base du triangle, changer le caractère de empty_char_mid
        if empty_mid == height * 2 - 2:
            empty_char_mid = "_" * empty_mid

        # Dessiner le triangle
        print(f"{empty_char}{l_diag}{empty_char_mid}{r_diag}")

        # Elargir l'espace à l'intérieur du triangle
        empty_side -= 1
        empty_mid += 2

# Prendre la hauteur en input
try:
    hauteur = int(input("Entrez la hauteur du triangle : "))
    triangle(hauteur)
except ValueError:
    print("Veuillez entrer un nombre entier valide pour la hauteur.")
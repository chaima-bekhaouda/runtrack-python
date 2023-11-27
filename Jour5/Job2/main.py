def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("Les dimensions sont trop petites pour former un rectangle.")
        return

    # Dessiner la première ligne avec des '-' et des coins '|'
    print("|" + "-" * (width - 2) + "|")

    # Dessiner les lignes du milieu remplies d'espaces
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Dessiner la dernière ligne avec des '-' et des coins '|'
    if height > 1:
        print("|" + "-" * (width - 2) + "|")

# Exemple d'utilisation avec width = 10 et height = 3
draw_rectangle(10, 3)



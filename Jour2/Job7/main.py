chaine = "abcdefghijklmnopqrstuvwxyz"
n = 10  # Nombre de lignes de la suite pyramidale

for i in range(1, n + 1):
    espace = " " * (n - i)  # Espace pour aligner la pyramide à droite
    caracteres = ' '.join(chaine[:i])  # Sélection des caractères jusqu'à la position i
    print(espace + caracteres + ' ' + caracteres[::-1][1:])  # Affichage de la ligne de la pyramide



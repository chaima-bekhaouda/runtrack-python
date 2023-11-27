# Définition de la fonction 'even_odd' avec un paramètre 'num'
def even_odd(num):
    # Vérifie si 'num' est négatif ou a une partie décimale (non entier)
    if num < 0 or num % 1 != 0:
        print("Invalide")
    # Vérifie si 'num' est un nombre pair
    elif num % 2 == 0:
        print("pair")
    # Si 'num' n'est ni négatif ni un nombre pair, il est impair
    else:
        print("impair")

# Appels de la fonction 'even_odd' avec différentes valeurs de 'num'
even_odd(0.4)  # Affiche "Invalide" car 0.4 a une partie décimale
even_odd(-15)  # Affiche "Invalide" car -15 est négatif
even_odd(4)    # Affiche "pair" car 4 est un nombre pair
even_odd(7)    # Affiche "impair" car 7 est un nombre impair

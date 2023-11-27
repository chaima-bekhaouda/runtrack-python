def distance_toilets(marches, hauteur):
    # Calcul de la distance parcourue pour descendre et remonter une fois
    distance_journaliere = (2 * marches * hauteur) / 100  # Convertir en mètres

    # Calcul de la distance hebdomadaire
    distance_hebdomadaire = distance_journaliere * 5 * 7  # 5 fois par jour, 7 jours par semaine

    return distance_hebdomadaire

# Exemple d'utilisation avec x marches de y cm
x_marches = 50
y_cm = 20
distance = distance_toilets(x_marches, y_cm)

print(f"Pour {x_marches} marches de {y_cm} cm, le gardien parcourt {distance:.2f} m par semaine.")

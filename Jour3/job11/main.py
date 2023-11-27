# Définition de la fonction 'time_to_text' avec un paramètre 'num' représentant la durée en minutes
def time_to_text(num):
    # Calcul des heures et des minutes à partir de 'num'
    hour = num // 60
    mins = num - (hour * 60)
    
    # Affichage du temps en texte en fonction des heures et des minutes calculées
    if hour == 0:
        print(f"{mins} minutes")
    elif hour == 1:
        print(f"{hour} heure et {mins} minute")
    else:
        print(f"{hour} heures et {mins} minutes")

# Appels de la fonction 'time_to_text' avec différentes valeurs de 'num'
time_to_text(61)    # Affiche "1 heure et 1 minute" car 61 minutes
time_to_text(3600)  # Affiche "60 heures" car 3600 minutes
time_to_text(159)   # Affiche "2 heures et 39 minutes" car 159 minutes
time_to_text(9)     # Affiche "9 minutes" car 9 minutes

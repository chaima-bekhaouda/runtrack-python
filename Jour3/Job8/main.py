def food(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Aucune correspondance trouvée")


# Appels de la fonction 'food' avec différentes combinaisons de type et de saison
food("fruits", "hiver")
food("fruits", "ete")
food("legume", "hiver")
food("legume", "ete")
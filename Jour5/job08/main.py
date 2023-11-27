def my_sort(lst):
    """
    Trie une liste dans l'ordre croissant en utilisant l'algorithme de tri par sélection.
    
    Args:
    lst (list): La liste à trier.
    
    Returns:
    list: La liste triée.
    """
    coups = 0  # Initialiser le compteur de coups
    
    # Parcourir la liste
    for i in range(len(lst)):
        # Trouver l'indice du minimum dans la partie non triée de la liste
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        
        # Échanger l'élément minimum avec le premier élément non trié
        lst[i], lst[min_index] = lst[min_index], lst[i]
        coups += 1  # Incrémenter le compteur de coups
    
    # Afficher le nombre total de coups nécessaires pour trier la liste
    print(f"Nombre total de coups nécessaires : {coups}")
    
    return lst  # Retourner la liste triée

# Exemple d'utilisation
ma_liste = [100, 4, 7, 13, 20, 1542]
resultat = my_sort(ma_liste)
print("Liste triée :", resultat)
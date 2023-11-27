# Liste de nombres à virgule flottante
numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Créer une nouvelle liste avec les nombres arrondis vers le bas (convertis en entiers)
rounded_numbers = [int(num) for num in numbers]  # Transforme les floats en integers

# Initialiser une variable n pour stocker la longueur de la liste
n = 0
for _ in rounded_numbers:
    n += 1

# Implémenter l'algorithme de tri à bulles pour trier la liste des nombres arrondis
for i in range(n):
    for j in range(0, n-i-1):
        if rounded_numbers[j] > rounded_numbers[j+1]:
            # Échanger les éléments s'ils ne sont pas dans l'ordre croissant
            rounded_numbers[j], rounded_numbers[j+1] = rounded_numbers[j+1], rounded_numbers[j]

# Afficher la liste triée
print(rounded_numbers)
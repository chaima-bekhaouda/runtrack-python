
# Afficher les tables de multiplication de 1 à N
for i in range(1, N + 1):
    print(f"\nTable de multiplication pour {i} :")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")

# Demander à l'utilisateur de saisir un entier supérieur à zéro (N)
while True:
    try:
        N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez saisir un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez saisir un nombre entier valide.")

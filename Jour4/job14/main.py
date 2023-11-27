import string

def my_long_word(num, input_string):
    # Diviser la chaîne en mots et retirer la ponctuation de chaque mot
    words = [
        word.strip(string.punctuation)
        for word in input_string.split()  
        # Filtrer les mots dont la sous-chaîne à partir de l'indice num est non vide
        if word.strip(string.punctuation)[num:]
    ]
    
    # Retourner une chaîne contenant les mots filtrés
    return ' '.join(words)

# Exemple d'utilisation
input_str = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, input_str)
print(resultat)

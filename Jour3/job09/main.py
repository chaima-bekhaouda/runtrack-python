# Définition de la fonction moyenne
def moyenne(note1, note2, note3):
    """
    Cette fonction prend trois notes en paramètre
    et retourne la moyenne de ces notes.
    """
    # Calcul de la moyenne
    moyenne_etudiant = (note1 + note2 + note3) / 3
    return moyenne_etudiant

# Demander à l'utilisateur de saisir trois notes
note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

# Appeler la fonction moyenne avec les notes saisies
moyenne_etudiant = moyenne(note1, note2, note3)

# Afficher la phrase en fonction de la moyenne de l'étudiant
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
else:
    print("Erreur : La moyenne n'est pas dans la plage attendue.")
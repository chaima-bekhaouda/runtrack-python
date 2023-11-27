def arrondir_notes(liste_notes):
    notes_arrondies = []
    for note in liste_notes:
        if note < 40:
            # Élève échoué, pas d'arrondi nécessaire
            notes_arrondies.append(note)
        else:
            # Élève réussi, vérification des critères d'arrondi
            difference = note % 5
            if difference >= 3:
                # Arrondir à la hausse au prochain multiple de 5
                note_arrondie = note + (5 - difference)
            else:
                # Pas d'arrondi nécessaire
                note_arrondie = note
            notes_arrondies.append(note_arrondie)
    return notes_arrondies

# Exemple d'utilisation :
liste_de_notes = [58, 83, 73, 18, 23, 48]
notes_arrondies = arrondir_notes(liste_de_notes)
print(notes_arrondies)
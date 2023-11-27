def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                message_chiffre += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
            else:
                message_chiffre += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
        else:
            message_chiffre += char
    return message_chiffre

# Exemple d'utilisation
message_original = "hello world"
decalage = 3    
message_chiffre = chiffrement_cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_chiffre)

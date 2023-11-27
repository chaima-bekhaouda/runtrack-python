def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro impossible"
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur invalide"

result_addition = calcule(5, '+', 3)
result_multiplication = calcule(10, '*', 2)
result_division = calcule(8, '/', 4)

print("Résultat A:", result_addition)
print("Résultat B:", result_multiplication)
print("Résultat C:", result_division)


def invertir(s):
    return s[::-1]

def es_palindrom(s):
    if s == invertir(s):
        return True
    else:
        return False

s = input("Introdueix una cadena: ")
a = invertir(s)
if es_palindrom(s):
    print("la frase/paraula {} es igual a {} i per tant es palindrom".format(s, a))
else:
    print("La frase/paraula {} no es igual a {} per tant no es palindrom".format(s, a))

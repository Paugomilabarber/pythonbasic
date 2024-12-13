#def funcio filtrar paraules 

def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix una paraula: ")
        if a != ".":
            l.append(a)
    return l

def filtre(llista, n):
    return list(filter(lambda paraula: len(paraula) > n, llista))

# programa principal
x = llegir_llista()
y = int(input("Introdueixi un numero: "))
resultat = filtre(x, y)
print("De la llista {} que tengui mes de {} caracters hi ha {} ".format(x, y, resultat))

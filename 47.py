

def llegir_llista():
    l = []
    a="a"
    while a!=".":
        a=input("Introduexi un numero: ")
        if a!=".":
            l.append((a))
    return l

def esta_ordenada(l):
    ld=l.sort(reverse=True)
    la=l.sort(reverse=False)
    if l.sort(reverse=True)==ld:
        print("La llista esta prdenada de forma descendent  ")
    elif l.sort(reverse=False)==la:
        ("Print la llista esta ordenada de forma ascendent  ")
    else:
        ("La llista esta desordenada")


#Programa principal
l=llegir_llista()
esta_ordenada(l)
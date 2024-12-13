def llegir_llista():
    #Precondicio: llegir un input
    #Postcondicio: si s'escriu punt s'acaba
    l = []
    a="a"

    while a!=".":
        a=input("Introduexi una paraula: ")
        if a!=".":
            l.append(a)
    return l

def elimina_duplicats(l):
    s = set(l)
    return(s)

l=llegir_llista()
r=elimina_duplicats(l)
print("La llista {} queda aixi {} ".format(l,r))
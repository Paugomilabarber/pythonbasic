

def llegir_llista():
    l = []
    a="a"
    while a!=".":
        a=input("Introduexi un numero o paraula: ")
        if a!=".":
            l.append((a))
    return l

def retorn_nova_llista(l):
    return l[1:-1]


#programa princpial
l=llegir_llista()
s=retorn_nova_llista(l)
print("{} es transforma en {}".format(l,s))
def llegir_llista():
    l = []
    a="a"
    while a!=".":
        a=input("Introduexi una llista de paraules: ")
        if a!=".":
            l.append((a))
    return l

def index_paraula(l, paraula):
    if paraula not in l:
        return -1
    else:
        for i,e in enumerate(l):
            if e==paraula:
                return i

#Programa principal
l=llegir_llista()
p=input("Dir que vols cercar: ")
n=index_paraula

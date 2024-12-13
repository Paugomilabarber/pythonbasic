#def paraulamesllarga i dir la mes llarga i quantes n'hi ha

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l


def paraula_de_cada_longitut(l):
    a = []
    c = []
    for e in l:
        a.append(len(e))
    b = set(a)
    for e in b:
        y = len(list(filter(lambda x:x==e,a)))
        a.append([e,y])
    return c


#Programa principal
a = llegir_llista()
print("la paraula mes llarga de la llista {} es {}".format(a, paraula_de_cada_longitut(a)))


#def paraulamesllarga i dir la mes llarga
"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l

def paraulamesllarga(l):
    a = l[0]
    for e in l:
        if len(e) > len(a):
            a = e
    return a


#Programa principal
a = llegir_llista()
print("la paraula mes llarga de la llista {} es {}".format(a, paraulamesllarga(a)))
"""
#DEF una funcio de numeros que comencin per (x) que donat una llista de noms
#ens digui quants comencen per la lletra a

"""
def llegir_llist():
    l = []
    a="a"

    while a!=".":
        a=input("Introduexi un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_que_comencen_per(l,c):
    m=[]
    for e in l:
        if e[-1:]==c.upper() or e[-1:]==c.lower() in l:
            m.append(e)
    print("Els elements de la llista {} que acaban per {} son: {} ".format(l,c,m))



#programa principal
l = llegir_llist()
c = input("Introdueixi un caracter: ")
noms_que_comencen_per(l,c)
"""

#Comparar  

def llegir_llist():
    l = []
    a="a"
    while a!=".":
        a=input("Introduexi un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_que_comencen_per(l,c):
    m=[]
    for e in l:
        senar = len(e)%2==1
        if senar:
            aux= len(e)//2
        if e[aux]==c.upper() or e[aux]==c.lower():
            m.append(e)
        else:
            aux = len(e)//2 -1
        if e[aux]==c.upper() or e[aux]==c.lower() or e[aux+1]==c.upper() or e[aux+1]==c.lower():
            m.append(e)
    print("Els elements {} de la llista que tenen {} son: {} ".format(l,c,m))

#programa principal
l = llegir_llist()
c = input("Introdueixi un caracter: ")
noms_que_comencen_per(l,c)
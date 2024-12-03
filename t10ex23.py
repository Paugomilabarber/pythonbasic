def llegirllista():
    l=[]
    a="a"
    while a!=".":
        a = input("Introdueix un numero de la llista: ")
        if a!=".":
            l.append(int(a))
    return (l)

def crear_punts(l):
    s="."
    for e in l:
        print(" {} \n".format(s*e))
    s="."

#Programa principal
a= llegirllista()
crear_punts(a)
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def gran_llista(l):
    return max(l)

#Programa principal
a = llegir_llista()
print("El major de la llista {} es {}".format(a, gran_llista(a)))

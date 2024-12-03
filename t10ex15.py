#calcular longitut de llista

def llegirllista():
    l=[]
    a="."
    while a!=".":
        a = input("Introdueix un numero de la llista: ")
        if a!=".":
            l.append(int(a))
    return (l)

def longitut(l):
    i=0
    for e in l:
        i +=1
    return i

#programa principal
x = llegirllista()
print(longitut(x))

#funcio de comptar vocals de un input i el resultat


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

def vocals(p):
    ap = [0,0,0,0,0]
    for e in p:
        if e == "a" or e == "A":
            ap[0]+=1
        elif e == "e" or e == "E":
            ap[1]+=1
        elif e == "i" or e == "I":
            ap[2]+=1
        elif e == "o" or e == "O":
            ap[3]+=1
        elif e == "u" or e == "U":
            ap[4]+=1
        else:
            print("{} no te vocals")
    print("La vocal {} apareix {} vegades \n la vocal eapareix {} vegades")#falta
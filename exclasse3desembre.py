#Llegir una cadena de caracters i substituir MAJUSCULES per .
# I mostrar resultat

s = input("Introdueix una cadena de caractes: ")
l = list(s)
r=[]
for e in l:
    if e in "ABCDEFGHIJKLMNOPQRSTUVWXZY":
        r.append("-")
    else:
        r.append(e)
s = " ".join(r)
print(s)


#Llegir una cadena de caracters i substituir vocals per .
# I mostrar resultat
"""
#funció que ens dir si un caracter es o no una vocal
def esvocal(x):
    return x.lower() in "aeiou"

#funcio per afegir punt
def punts(p):
    resultat = ""
    for e in p:
        if esvocal(e):
            resultat += "."
        else:
            resultat += e
    return resultat

#Programa principal
a = "a"
while(a != "."):
    a = input("Escriu una cadena de caràcters: ")
    if a != ".":
        frase_alterada = punts(a)
        print("La frase alterada és: {}".format(frase_alterada))
"""
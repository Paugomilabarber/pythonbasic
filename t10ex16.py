#funció que ens diu si un caracter es o no una vocal
def esvocal(x):
    return x.lower() in "aeiou"
#proves amb diferents caracters
a = "a"
while(a!="."):
    a = input("Escriure la lletra: ")
    if esvocal(a):
        print("La lletra introduida {} és vocal".format(a))
    else:
        print("La lletra introduida {} no es vocal".format(a))

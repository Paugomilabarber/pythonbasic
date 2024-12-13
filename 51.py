
def crear_llista_fitxer(nom):
    l=[]
    with open(nom,"r") as f:
        for line in f:
            l.append(line[:-3])
        return l
    
#programa principal
l=crear_llista_fitxer("PROVA1.txt")
print(l)

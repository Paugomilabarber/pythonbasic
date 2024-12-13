def index_paraula(llista, paraula):
    if paraula in llista:
        return llista.index(paraula)
    else:
        return -1

# Programa principal
llista_input = input("Introdueix una llista de paraules separades per espais: ")
llista = llista_input.split()
llista.sort()

paraula = input("Introdueix la paraula que vols cercar: ")

# Cercar l'índex de la paraula
index = index_paraula(llista, paraula)

# Mostrar el resultat amb format
if index != -1:
    print("L'índex de la paraula '{}' és: {}".format(paraula, index))
else:
    print("La paraula '{}' no es troba a la llista.".format(paraula))

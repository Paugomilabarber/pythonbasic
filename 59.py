def es_primer(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Llista de números de l'1 al 100
numeros = range(1, 101)


primers = list(filter(es_primer, numeros))

# Imprimir els resultats
print("Els números primers entre 1 i 100 són: {}".format(primers))
print("Hi ha un total de {} números primers entre 1 i 100.".format(len(primers)))

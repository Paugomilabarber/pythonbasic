def crear_llista_fitxer(fl):
    llista = []
    paraula = open(fl, "r")
    for line in paraula:
        for word in line.split():
            llista.append(word.strip())
    paraula.close()
    return llista

print(crear_llista_fitxer("words.txt"))
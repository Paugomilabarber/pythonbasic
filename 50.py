def elimina_duplicats(llista):
    llista_sense_duplicats = []
    for element in llista:
        if element not in llista_sense_duplicats:
            llista_sense_duplicats.append(element)
    return llista_sense_duplicats

llista = [1, 2, 2, 3, 4, 4, 5, 1]
llista_sense_duplicats = elimina_duplicats(llista)
print("Llista original:", llista)
print("Llista sense duplicats:", llista_sense_duplicats)

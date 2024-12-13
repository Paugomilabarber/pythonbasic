def crear_llista_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            contingut = fitxer.read()
            llista_paraules = contingut.split()
        return llista_paraules
    except FileNotFoundError:
        print(f"Error: El fitxer {nom_fitxer} no existeix.")
        return []


nom_fitxer = 'exemple.txt'
llista_paraules = crear_llista_fitxer(nom_fitxer)
print("Paraules del fitxer:", llista_paraules)

def elements_parells(llista):
    return [paraula for i, paraula in enumerate(llista) if i % 2 == 0]

# Programa principal
llista_input = input("Introdueix una llista de paraules separades per espais: ")
llista = llista_input.split()

resultat = elements_parells(llista)

print("Les paraules en posicions parells són: {}".format(resultat))

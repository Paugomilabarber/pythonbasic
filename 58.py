# Funció que imprimeix el patró amb una lambda
imprimir_patro = lambda x: [print(' '.join(map(str, range(i, 0, -1)))) for i in range(x, 0, -1)]

# Chamar la funció amb el valor 5
imprimir_patro(5)

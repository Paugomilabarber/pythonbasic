def suma_numeros(inici, final):
    suma_total = 0
    for num in range(min(inici, final), max(inici, final) + 1):
        suma_total += num
    return suma_total

# Programa principal
inici = int(input("Introdueix el número inicial: "))
final = int(input("Introdueix el número final: "))

resultat = suma_numeros(inici, final)

print(f"La suma de tots els números entre {inici} i {final} és: {resultat}")

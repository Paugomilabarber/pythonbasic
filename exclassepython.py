#dos inputs i distigir la paraula mes llarga
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

# programa principal
if len(paraula1) > len(paraula2):
    print("La paraula més llarga és: {}".format(paraula1))
elif len(paraula1) < len(paraula2):
    print("La paraula més llarga és: {}".format(paraula2))

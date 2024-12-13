# Mostrar números parells (pares) fins a 100
print("Números parells fins a 100:")
for i in range(2, 101, 2):
    if i == 100:
        print(i)
    else:
        print(i, end=", ")

# Mostrar números senars (impares) fins a 100
print("\n Números senars fins a 100:")
for i in range(1, 100, 2):
    if i == 99:
        print(i)
    else:
        print(i, end=", ")

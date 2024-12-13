x = int(input("Introdueixi un numero menor a 100:   "))
y = 0.0
for i in range(x,1,-4):
    y += i**2
    print("La suma del quadrats de 4 en 4 de {} es {}".format(x,y))
else:
    print("No es menor a 100")
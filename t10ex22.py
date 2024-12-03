def crear_repetits(n,c):
    return c*n


#Programa principal
a= input("Introdueix un caracter: ")
b=  int(input("Introdueixi el numero de vegades que vulgui repetir: "))
print("El caracter {} repetit {} vegades es {}".format(a,b,crear_repetits(b,a)))

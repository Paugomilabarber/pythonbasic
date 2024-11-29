def menu():
    print("MENÚ CALCULADORA: ")
    print("1. sumar en decimal")
    print("2. restar en decimal")
    print("3. multiplicar en decimal")
    print("4. dividir en decimal")
    print("5. traducir decimal a binario")
    print("6. traducir decimal a hexadecimal")
    print("7. traducir decimal a octal")
    print("8. salir")
    
    op = int(input("Introduce una opción: "))
    return op

def sumar():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    c = a + b
    print("El resultado de sumar {} más {} es: {}".format(a, b, c))

def restar():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    c = a - b
    print("El resultado de restar {} menos {} es: {}".format(a, b, c))

def multiplicar():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    c = a * b
    print("El resultado de multiplicar {} por {} es: {}".format(a, b, c))

def dividir():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    if b != 0:
        c = a / b
        print("El resultado de dividir {} entre {} es: {}".format(a, b, c))
    else:
        print("No se puede dividir por cero.")

def convertir_desde_decimal(tipo):
    numero = int(input("Introduce el número decimal: "))
    if tipo == "binario":
        return bin(numero)[2:]
    elif tipo == "hexadecimal":
        return hex(numero)[2:]
    elif tipo == "octal":
        return oct(numero)[2:]
    else:
        print("Tipo no válido")
        return None

def traducir(tipo):
    resultado = convertir_desde_decimal(tipo)
    if resultado is not None:
        print("El número decimal convertido a {} es: {}".format(tipo, resultado))

a = True

while a:
    op = menu()
    match op:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
            traducir("binario")
        case 6:
            traducir("hexadecimal")
        case 7:
            traducir("octal")
        case 8:
            a = False

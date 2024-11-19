def mostra_menu():
    resta_numeros_enters()           ("""Menú del programa principal:
            1. Calculadora de números sencers: suma
            2. Calculadora de números sencers: resta
            3. Calculadora de números sencers: multiplicació
            4. Calculadora de números sencers: divisió entera 
            5. Calculadora de números sencers: resta de la divisió entera
            6. Calculadora de números sencers: potència
            7. Calculadora de números reals: suma
            8. Calculadora de números reals: resta
            9. Calculadora de números reals: multiplicació
            10.Calculadora de números reals: divisió real
            11.Calculadora de números reals: potència
            12. Sortir
""")
""""""

op = input("Elegeixi una opció del menú")
def suma_numeros_enters():
    print("Estic sumant numeros enters \n")
    a = int(input("Introdueixi el primer número: "))
    b = int(input("Introdueixi el segon número: "))
    print("La suma de {} i {} és {}".format(a, b, a+b))


def resta_numeros_enters():
    print("Estic restant numeros enters \n")
    a = int(input("Introdueixi el primer número: "))
    b = int(input("Introdueixi el segon número: "))
    print("La suma de {} i {} és {}".format(a, b, a-b))

def multiplicació_numeros_enters():
    print("Estic multiplicant numeros enters \n")
    a = int(input("Introdueixi el primer número: "))
    b = int(input("Introdueixi el segon número: "))
    print("La suma de {} i {} és {}".format(a, b, a*b))
#seguir amb altres operacions enteras i reals


#Programa pricipal
x = mostra_menu()

match(op)
    case "1":
        Suma_numeros_enters()
    case "2":
        resta_numeros_enters()
    case "3":
        multiplicació_numeros_enters()
    case "4":
        resta_numeros_enters()
    case "5":
        resta_numeros_enters()
    case "6":
        resta_numeros_enters()
    case "7":
        resta_numeros_enters()
    case "8":
        resta_numeros_enters()
    case "9":
        resta_numeros_enters()
    case "10":
        resta_numeros_enters()
    case "11":
        potencia numeros_reals()
    case "12":
        print("Sortir")
    else :
        return (op)

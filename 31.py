#def funcio que mostra major i que amb una tupla de enters imprimeixi el superior de numero donat

"""
def llegir_llist():
    l = []
    a="a"

    while a!=".":
        a=input("Introduexi un numero: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors(t, num):
    for e in t:
        if e > num:
            print("{} es major que {} ". format(e, num))
    

#programa principal
x = llegir_llist()
y = tuple(x)
num = int(input("Introdueixi el numero a comparar: "))
mostrar_majors(y, num)
"""

#VARIANT
"""
def llegir_llist():
    l = []
    a="a"

    while a!=".":
        a=input("Introduexi un numero: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors(t, min, max):
    for e in t:
        if  e>min and e<max:
            print("{} es major que {} i menor que {} ". format(e, min, max))
    

#programa principal
x = llegir_llist()
y = tuple(x)
min = int(input("Introdueixi el numero minim a comparar: "))
max = int(input("Introdueixi el numero maxim a comparar: "))
mostrar_majors(y, min, max)
"""

#Programacio funcional (acabada i es correcte)

def llegir_llist():
    l = []
    a="a"

    while a!=".":
        a=input("Introduexi un numero: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors(t, min, max):
    print("El numeros entre aquest dos son: {}". format(list(filter(lambda x: x>min and x<max,t))))
    

#programa principal
x = llegir_llist()
y = tuple(x)
min = int(input("Introdueixi el numero minim a comparar: "))
max = int(input("Introdueixi el numero maxim a comparar: "))
mostrar_majors(y, min, max)


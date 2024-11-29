#Parametres
#String o cadena de caracters
def modifica_string(s):
    s="Això es un canvi"

s="Bon dia"
print(s)
modifica_string(s)
print(s)
#despres de la prova veim que passa valor (no canvia el tipus)


#tipus parametres
def operacio(a, b, c):
    c = a + b
a = 3
b = 4
c = 0
print(c)
operacio(a, b, c)
print(c)


#2~per referencia i sí que modifica el valor

def aXllista(l):
    for i in range (len(l)):
        l[i]*=3

#programa principal del 2~
llista=[3,4,5]
print (llista)
aXllista(llista)
print(llista)

 #escriure un programa que converti els binaris en enters

def binari(b):
    aux = b[::-1]
    d=0
    for i,e in enumerate(b):
        d+= int(e)*(2**i)
    return d

a = input("Introdueix un numero en binari (0s i 1s) :  ")
print("El numero {} a decimal es {} ". format(a,binari(a)))

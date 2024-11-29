#fer el factorial de forma iterativa
n = int(input("Introdueixi un numero per fer el factorial: "))
r=1
while(n>0):
    r=r*n
    n=n-1
print(r)

#fer el factorial en recursivitat
def factorial(n):
    if n<=0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

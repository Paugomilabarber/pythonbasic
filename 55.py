


x=int(input("Escriu el menor: "))
y=int(input("Escriu el major: "))
suma=0
for i in range(x,y+1,1):
    if i&2==0:
        suma+=1
print(suma)

#ex. multiplicar per 3 tota una llista
l = [3, 4, 5, 7, 10]

#solució utilitzant un bucle
r=[]
for e in l:
    r.append(e*3)
print(r)

#solucio utilitzant funcio anonima (lambda) i map
#programacio funcional
r = list(map(lambda x: x*3, l))
print (r)

#solució utilitzant map i funció normal
def pertres(x):
    return x*3
r=list(map(pertres, l))
print (r)

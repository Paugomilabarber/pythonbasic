#ex. elevar per 5 tota una llista
l = [3, 4, 5, 7, 10]

#solució utilitzant un bucle
r=[]
for e in l:
    r.append(e**5)
print(r)

#solucio utilitzant funcio anonima (lambda) i map
#programacio funcional
r = list(map(lambda x: x**5, l))
print (r)

#solució utilitzant map i funció normal
def pertres(x):
    return x**5
r=list(map(pertres, l))
print (r)

#Una llista que retorni es numeros parells
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#versió iterativa
r=[]
for e in l:
    if e%2==0:
        r.append(e)
print (r)

#versió amb filter (funcional)
def parell(x):
    if x%2==0:
        return True
    return False
w=list(filter(parell, l))
print(w)

#versió amb funció anònima pero impar
s=list(filter(lambda x:x%2==1, l))
print(s)

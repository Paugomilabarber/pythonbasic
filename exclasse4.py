def llista_descendent():
    l=[]
    a=True
    u = input("Introdueixi el primer número: ")
    l.append(u)
    while a:
        c = input("Introdueixi un número: ")
        if c>u:
            a=False
        else:
            l.append(c)
    return l

#programa principal
l = llista_descendent()
print("La llista de numeros descendents es {}".format(l))



"""
def llegir_llista():
    l=[]
    p=""
    while p!=".":
        p=input("Introdueixi un element de la llista: ")
        if p!=".":
            l.append(int(p))
    return l

#programa principal
llista = llegir_llista()
r=[]
for i,e in enumerate(llista):
    if i==e:
        r.append(e)
print("La llista d'elements que coincideixi element i posició és {}".format(r))
"""
p = ""
l = []
while p != ".":
    p = input("Introdueixi una frase: ")
    if p != ".":
        s = p.title()
        l.append(s)
print("Les frases introduïdes són: {}".format(l))
print("Ja hem acabat!")




"""
p=""
l=[]
while (p!="."):
    p = input("Introdueixi una paraula: ")
    if p!="." and len(p)==4:
        l.append(p)
    if len(l)==4:
        p="."
print("Les paraules son: {}".format(l))
print("Ja hem acabat!")
"""
p=""
l=[]
while (p!=":"):
    p = input("Introdueixi una paraula: ")
    if p!=":" and p[0]=="A":
        l.append(p)
    if len(l)==4:
        p="."
print("Les paraules que comencen per A son: {}".format(l))
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
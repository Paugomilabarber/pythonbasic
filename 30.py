#escriure un programa que calculi els anys que cumplira segons l'input i les dades les donin tabulades
"""
exemple:

Any actual: 2024
nom         data neixement      anys que fara
pere            2000                24
pau             2008                16
oscar           2007                17
toni            2007                17

"""


a = "2024"
d=[]
l=[]
for i in range(4):
    d.append(input("Indica el teu nom: "))
    d.append(input("Indica l'any (aaaa) que vas neixer:  "))
    l.append(d)
    d.clear()
a=""
print(" {:<20}  {:<20}  {:<20}".format("Nom","Data naixement","Anys que tindra aquest any "))
for e in l:
    print("\t {:<20}  \t {:<20}  \t {:<20} ".format(e[0],e[1],int(a)-int(e[1])))

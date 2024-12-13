#programa detector de rimes

x=input("Introdueixi una paraula per rimar: ")
y=input("Introdueixi la segona paraula per rimar: ")
if x[-3:]==y[-3:]:
    print("{} i {} rimen".format(x,y))
else:
    print("Les paraules no rimen")
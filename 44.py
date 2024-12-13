

x = input("Intro num:")
sum=0
for e in x:
    sum+int(e)
if sum%2==0:
    print("La suma dels dígits del numero {} es {} i es parell".format(x, sum))

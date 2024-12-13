#MASTERMIND
#es al classrom com tot
import random
print("BENVINGUT A MASTERMIND")

def crearnumeros():
    l=[]
    for i in range(4):
        l.append(random.randint(0,9))
    return l

def comparar(l):
    s=[]
    r=[0, 0, 0, 0]
    for i in range(4):
        s.append(int(input("NUM:  ")))
        if l[i]==s[i]:
            r[i]=2
    


#programa principal
m = crearnumeros()

print(m)


import random

def llista_20():
    l=[]
    for i in range(20):
        l.append(random.randint(1,100))
    return l

l=llista_20()
print(l)
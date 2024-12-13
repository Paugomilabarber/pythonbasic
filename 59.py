"""
for i in range(1,101):
    if i%2!=0:

print(i)
"""
def primers(max):
    print(1)
    for i in range(2, max+1):
        primer = True
        for j in range(2,i):
            if (i%j == 0):
                primer = False

        if primer:
            print(i)      
    
primers(100)

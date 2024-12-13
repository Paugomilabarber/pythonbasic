

x = int(input("Quantitat:   "))
i = float(input("Interes:    "))
a = int(input("Numero d'anys:   "))
c = x * (1+i/100)**a
print("Amb el capital {} € amb un interes de {} % per {} anys, al final es convertira en {}€ ".format(x,i,a,c))
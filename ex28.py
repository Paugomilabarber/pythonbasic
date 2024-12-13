
def num_majuscules(s):
    num=0
    j=[]
    for e in s:
        #if e in "QWERTYUIOPASDFGGHJKLÑZXCVBNM"
        if e.isupper():
            num += 1
            j.append(e)
    return num,"".join(j)

#programa principal
a = input("INTRODUEIXI UNA PARAULA AMB MAJUSCULES I MINUSCULES: ")
print("El numero de majuscules que te la paraula {} es {} ".format(a,num_majuscules(a)))

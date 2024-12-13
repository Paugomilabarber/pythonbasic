with open("PROVA1.txt","w") as f:
    for i in range(10):
        f.writelines(str(i+1))

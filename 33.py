#Varietat de l'exercici anterior pero modificam perque compari els caracters centrals entre ells
#FER-HO EN PROGRAMACIÓ FUNCIONAL
#Precondicio: 
#Postcondicio:

def llegir_llista():
    #Precondicio: 
    #Postcondicio:
    l = []
    a="a"

    while a!=".":
        a=input("Introduexi un nom: ")
        if a!=".":
            l.append(a)
    return l

def retorna_conjunt():
    #Precondicio: 
    #Postcondicio:
    m=[]
    for e in l:
        senar = len(e)%2==1


#PROGRAMA PRINCIPAL
#Precondicio: 
#Postcondicio:
l = llegir_llista()
s = retorna_conjunt(l)
llistes_comparades(l,s)


def primedetector(entry):
    
    if n == 1:
        return False
    elif n < 10:
        for i in range(2, n):
            if n % i == 0:
                return False 
    elif n >= 10:
        for i in range(2,int(n**0.5)):
            if n % i == 0:
                return False
    
    return True



onesnail = lambda s : 3*(10*s + 1) + 57

twosnail = lambda s: 3*s + 57

eulerprime = lambda n: n**2 + n + 41


yes = 0
no = 0

def onesnailfunc():
    global yes
    global no

    entry = int(input("vérifier de 0 jusqu'à ? (n > 0): "))

    print(f"onesnail 0 -> {entry}")

    for i in range(0,entry + 1):

        if primedetector(onesnail(i) - 1) == True or primedetector(onesnail(i) + 1) == True:
            yes = yes + 1

        else:
            no = no + 1


def twosnailfunc():
    global yes
    global no

    entry = int(input("vérifier de 0 jusqu'à ? (n > 0): "))

    print(f"twosnail 0 -> {entry}")

    for i in range(0,entry + 1):
        if primedetector(twosnail(i) - 1) == True or primedetector(twosnail(i) + 1) == True:
            yes = yes + 1

        else:
            no = no + 1

def eulerprimefunc():
    global yes
    global no

    entry = int(input("vérifier de 0 jusqu'à ? (n > 0): "))

    print(f"nombre chanceux euler 0 -> {entry}")

    for i in range(0,entry + 1):
        if primedetector(eulerprime(i)) == True:
            yes = yes + 1

        else:
            no = no + 1


#manuellement : enlever ou 1 commentaire pour la fonction que où on veut vérifié la probabilité pour être premier, et laissé les deux autre en commentaire

#eulerprimefunc() 
#onesnailfunc()
#twosnailfunc()

choose = int(input("""
quelle fonction voulez vous utiliser pour les probabilités :

[1] Euler nombres premiers chanceux
[2] Onesnail
[3] Twosnail

numéro ? : """))

if choose == 1:
    eulerprimefunc()
elif choose == 2:
    onesnailfunc()
elif choose == 3:
    twosnailfunc()
else:
    print("entré incorrecte")
    quit()


prob = (yes/(yes + no)) * 100
print(prob,"%")

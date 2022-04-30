yes = 0
no = 0

def primedetector(entry):

    if entry < 5:
      for i in range(2, entry):
        if entry % i == 0:
          return False
    
    for i in range(2, int((entry + 1)**0.5)):
        if entry % i == 0:
            return False
    return True

othersnail = lambda s : 20*s + 59 #fonciton modifiable

def othersnailfunc():
    global yes
    global no

    entry = int(input("vérifier de 0 jusqu'à ? (n > 0): "))

    print(f"othersnail 0 -> {entry}")

    for i in range(0,entry + 1):

        if primedetector(othersnail(i) - 2) == True or primedetector(othersnail(i) + 2) == True:
            yes = yes + 1

        else:
            no = no + 1

othersnailfunc()

prob = (yes/(yes + no)) * 100
print(prob,"%")

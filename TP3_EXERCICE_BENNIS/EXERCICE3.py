from random import*

x = randint(0, 100)
y = -1
z = 0

while y != x:
    y = int(input("Veuillez deviner le nombre : "))
    z +=1
    
    if y < x:
        print("Trop petit !")
        
    if y > x:
        print("Trop grand !")
    
    elif y == x:
        print("Félicitations !")
        
        break

print("Vous avez réussi au bout de", z ,"essais !")

    
    

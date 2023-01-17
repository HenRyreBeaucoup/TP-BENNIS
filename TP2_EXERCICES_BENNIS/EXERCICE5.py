n = int(input("Entrez un nombre entier : "))

if n > 0:
    if (n % 2) == 0:
       print("Le nombre est positif et pair".format(n))
    if (n % 2) == 1:
       print("Le nombre est positif et impair".format(n))
 
if n <0:
    if (n % 2) == 0:
       print("Le nombre est négatif et pair".format(n))
    if (n % 2) == 1:
       print("Le nombre est négatif et impair".format(n))

if n == 0:
        print("Le nombre est zéro (et il est pair)".format(n))
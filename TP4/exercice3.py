import math

nMax = 3
V1 = []
V2 = []

n = int(input(f"Choisir la taille des vecteur (entre 1 et {nMax}) : \n"))

while n < 1 or n > nMax:
    n = int(input(f"La taille des vecteurs n'est pas valide (entre 1 et {nMax})"))


for i in range(n):
    V1.append(int(input(f"Entrez la composante v1[{i}]")))
    V2.append(int(input(f"Entrez la composante v2[{i}]")))

produit_Scalable = 0
somme_carrees_V1 = 0
somme_carrees_V2 = 0
for i in range(n):
    produit_Scalable += V1[i] * V2[i]
    somme_carrees_V1 += V1[i] ** 2
    somme_carrees_V2 += V2[i] ** 2

norme_euclidienne_V1 = math.sqrt(somme_carrees_V1)
norme_euclidienne_V2 = math.sqrt(somme_carrees_V2)

print(f"Le produit scalaire de v1 par v2 vaut {produit_Scalable}")
print(f"La norme euclidienne de v1 est {norme_euclidienne_V1}")
print(f"La norme euclidienne de v2 est {norme_euclidienne_V2}")
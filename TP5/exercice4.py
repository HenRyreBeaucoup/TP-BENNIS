somme = int(input("Veuillez entrer la somme que vous désirez : \n"))

nombre_billets_100 = somme // 100
somme = somme % 100

nombre_billets_50 = somme // 50
somme = somme % 50

nombre_billets_10 = somme // 10
somme = somme % 10

nombre_pièces_2 = somme // 2
somme = somme % 2

nombre_pièces_1 = somme

print("Voici la somme d'argent de façon décomposée :")
print(f"- c'est {nombre_billets_100} billets de 100")
print(f"- c'est {nombre_billets_50} billets de 50")
print(f"- c'est {nombre_billets_10} billets de 10")
print(f"- c'est {nombre_pièces_2} pièces de 2 euros")
print(f"- c'est {nombre_pièces_1} pièces de 1 euros")
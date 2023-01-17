binome = ('login1', 'login2')

print(binome)

nouveau_login = str(input("Veuillez entrer le nouveau login souhaité : \n"))
binome = list(binome)
binome[1] = nouveau_login
binome = tuple(binome)

print(binome)

nouveau_login2 = str(input("Veuillez entrer le nouveau login à ajouter : \n"))
binome = list(binome)
binome.append(nouveau_login2)
binome = tuple(binome)

print(binome)
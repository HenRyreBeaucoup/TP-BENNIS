heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_total = 0

if heures_travaillees <= 160:
    salaire_total = heures_travaillees * salaire_horaire
elif heures_travaillees <= 200:
    salaire_total = 160 * salaire_horaire + (heures_travaillees - 160) * salaire_horaire * 1.25
else:
    salaire_total = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (heures_travaillees - 200) * salaire_horaire * 1.5

print("Salaire total :", salaire_total)
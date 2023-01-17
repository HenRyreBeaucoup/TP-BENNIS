numero_students = int(input("Donnez le nombre d'étudiants : "))
total = 0
student_grades = []
for i in range(numero_students):
    grade = float(input("Note étudiant {} : ".format(i)))
    student_grades.append(grade)
    total += grade

class_average = total / numero_students
print("Moyenne de classe : {:.2f}".format(class_average))
for i in range(numero_students):
    grade = student_grades[i]
    deviation = grade - class_average
    print("Numéro de l’étudiant {} | note {} | écart à la moyenne {:.2f}".format(i, grade, deviation))
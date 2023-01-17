def table_multiplication(n):
    table = []
    for i in range(1, 10):
        result = n*i
        table.append(f"{n} {i} = {result}")
    for i in range(0,9):
        print(table[i])

nombre = float(input("Vous cherchez la table de multiplication de quel nombre ?"))
table_multiplication(nombre)
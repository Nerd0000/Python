notas = []

for i in range(4):
    notas.append(float(input(f"Nota {i+1} ")))
print(notas)
print(sum(notas)/len(notas))
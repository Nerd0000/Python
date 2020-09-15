notasAlunos  = [] #notas armazenadas temporariamente
alunosAprovados = 0 #numero total de aprovados

for i in range(10):
    print(f"Aluno {i+1}")

    for i in range(4):
        notasAlunos.append(float(input(f"Nota {i+1}: ")))

    if sum(notasAlunos) >= 7:
        alunosAprovados += 1

    notasAlunos.clear()

print(f"{alunosAprovados} foram aprovados")

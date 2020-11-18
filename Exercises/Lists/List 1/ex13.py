def media():
    notas = []
    for i in range(5):
        notas.append(float(input(f"Numero {i+1}: ")))
    return sum(notas)/len(notas)
print(media())
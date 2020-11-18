numeros = [1,2,3,4,5,6,7,8,9,10,9192192912912,1,2,12,12,1,21,312,3,24,234,23,4,234,234,2,34,4]
pares = []

for i in range(len(numeros)):
    if numeros[i]%2 == 0:
        pares.append(numeros[i])

print(f"Dentre os dos {len(numeros)} números, {len(pares)} sao pares ")

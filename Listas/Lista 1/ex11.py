import random
ListaDeNumeros = []
par = []
impar = []

for i in range(50):
    ListaDeNumeros.append(int(100*random.random()))
for i in range(len(ListaDeNumeros)):
    if ListaDeNumeros[i]%2 == 0:
        par.append(ListaDeNumeros[i])
    else:
        impar.append(ListaDeNumeros[i])
print(par)
print(impar)
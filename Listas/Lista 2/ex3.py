ln = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
l3 = []
l5 = []

for i in range(len(ln)):
        if ln[i]%3 == 0:
            l3.append(ln[i])
        if ln[i]%5 == 0:
            l5.append(ln[i])

print(f'Dentre os {len(ln)} numeros, {len(l3)} sáo divisiveis por 3, e {len(l5)}  por 5')

'''def in_mult(num1, num2, num3, num4, num5):
    return num1*num2*num3*num4*num5
print(in_mult(1,2,3,4,5))
'''

def abacate():
    vetor = []
    mult = 1
    for i in range(5):
        vetor.append(float(input("Insira um número: ")))
    for i in range(4):
        mult = vetor[i]
    return mult
print(abacate())
numbers = [] #all the input nunbers.
mult = 1 #value of multiplication.

for i in range(5):
    numbers.append(float(input(f"Número {i+1}: ")))
    mult *= numbers[i] #multiply the saved value by where the list is

print(f"Os numeros dados foram: {numbers}")
print(f"Sua multiplicação resulta em: {mult}")
print(f"já sua soma resulta em: {sum(numbers)}")
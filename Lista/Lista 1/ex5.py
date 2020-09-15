numbers = []
even = []
odd = []

for i in range(20):
    numbers.append(float(input()))
    if numbers[i]%2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])

print(numbers)
print(even)
print(odd)
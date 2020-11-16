ln = []

for i in range(100, 800):
    if (int(str(i)[0]) + int(str(i)[2]))/2 == int(str(i)[1]):
        ln.append(i)

print(len(ln))
print(ln)

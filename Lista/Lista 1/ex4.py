def howManyConsoants(string):
    vogals = 'aeiouAEIOU'
    numbers = 0

    for i in range(len(string)):
        numbers += is_Consoant(string, vogals, i)
    return numbers


def is_Consoant(string, vogals, i):
    if string[i] in vogals:
        return 0
    else:
        return 1

print(howManyConsoants("abcdefghijklmnopqrstuvwxyz"))
cont = 0

def inv_verifier(val1, val2):
    for i in range(len(val1)):
        if i < len(val1)-1:
            if val1[i]*val2[i] == val1[i+1]*val2[i+1]:
                i += 1
            else:
                return False
    return True

def dir_verifier(val1, val2):
    for i in range(len(val1)):
        if i < len(val1)-1:
            if val1[i]/val2[i] == val1[i+1]/val2[i+1]:
                i += 1
            else:
                return False
    return True

def verifier(val1, val2):
    if len(val1) != len(val2):
        return 'Error, please put same range!'
    if dir_verifier(val1, val2) == True:
        return 'Diretamente'
    elif inv_verifier(val1, val2) == True:
        return 'Inversamente'
    else:
        return 'Não'

print(verifier([1,2,3,4], [9,4.5,3,2.25]))

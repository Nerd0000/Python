#---------------------------------------------- variables
cont = 0
val1 = []
val2 = []
question = False

#---------------------------------------------- code core
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
        print('\nError, please put same range!')
    if dir_verifier(val1, val2) == True:
        print('\nThe values are directly proportional')
    elif inv_verifier(val1, val2) == True:
        print('\nThe values are inversely proportional')
    else:
        print('\nThe values are not proportional')

#---------------------------------------------- user inputs
question = int(input('What is the range of the number?\n'))

for i in range(question):
    val1.append(float(input('\nPlease put the value: ' )))
    val2.append(float(input('Please put the correspondent value: ')))

verifier(val1, val2)

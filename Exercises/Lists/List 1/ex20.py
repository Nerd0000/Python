def contador(phrase, searching):
    cont = 0
    for i in phrase:
        if searching == i:
            cont+=1
    return cont
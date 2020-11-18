def contrario():
    return s[::1]

def MinParaMai(c):
    if c in 'abcdefghijklmnopqrstuvwxyz':
        return chr(ord(c)-32)
    return c

def MaiParaMin(c):
    if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return chr(ord(c)+32)
    return c


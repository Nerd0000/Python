'''This code will analize text, retruning stuff like'''

def string_formatizer(string):
    string = string.capitalize()
    string = string.strip()

def string_searcher(string, term):
    return string.count(chr(term+32)) + string.count(term)

print(string_formatizer('      ALBERTO PINHEIRES'))
print(string_searcher('ALBERTO PINHEIRES', 'e'))

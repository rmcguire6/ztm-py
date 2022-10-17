def revStr(str):
    if (type(str) != type('str')):
        return ('not a string')
    else:
        if (len(str) < 2):
            return str
        else:
            letters = ''
            for letter in str:
                letters = letter + letters
            return letters
print(revStr('o'))
print(revStr(4))
print(revStr('hello'))
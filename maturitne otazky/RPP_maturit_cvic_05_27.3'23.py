def prevrat(string):
    out = ''
    string = string.replace(' ', '')
    for i in range(len(string)):
        out += string[-(i+1)]
    return out

sentence = input()
if prevrat(sentence) == sentence.replace(' ', ''):
    print('Je palindrom')
else:
    print('Nie je palindrom')
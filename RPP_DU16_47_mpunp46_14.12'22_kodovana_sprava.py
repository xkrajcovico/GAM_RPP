vstup = str(input(f'>>'))
out = ''
for i in range(len(vstup)):
    if vstup[i].isdigit() == True:
        out += vstup[i+int(vstup[i])]
print(out)
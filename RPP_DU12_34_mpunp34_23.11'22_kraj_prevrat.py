def prevrat(retazec):
    out = ''
    for i in range(len(retazec)):
        out += retazec[-(i+1)]
    print(out)
prevrat(str(input()))
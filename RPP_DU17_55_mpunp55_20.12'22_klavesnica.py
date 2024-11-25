jed = ['a','d','g','j','m','p','t','w']
dva = ['b','e','h','k','n','q','u','x']
tri = ['c','f','i','l','o','r','v','y']
out = 0
vstup = str(input(f'   >>>'))
for znak in vstup:
    if znak in jed:
        out += 1
    elif znak in dva:
        out += 2
    elif znak in tri:
        out += 3
    else:
        out += 4
print(out)

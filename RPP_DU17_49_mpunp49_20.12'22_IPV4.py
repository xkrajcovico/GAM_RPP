ipv6 = input().strip().split('.')
ipv6 = list(map(int,ipv6))
ipv4 = []
for i in range(len(ipv6)):
    cislo = ''
    while ipv6[i] != 0:
        zvysok = ipv6[i] % 2
        cislo = str(zvysok) + cislo
        ipv6[i] = ipv6[i] // 2
    while len(cislo) != 8:
        cislo = '0' + cislo
    ipv4.append(cislo)
# ipv4 = list(map(int,ipv4))
out = ''
for i in range(len(ipv4)):
    out += ipv4[i] + '.'
print(out)
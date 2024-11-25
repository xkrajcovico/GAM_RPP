from random import randrange
l = []
n = int(input())
for i in range(n):
    if randrange(2) == 0:
        l.append('V')
    else:
        l.append('T')
print(l,'\npocet T: ',l.count('T'),'\npocet V: ',l.count('V'))
while l.count('T') != l.count('V'):
    if l.count('T') > l.count('V'):
        l.append('V')
    elif l.count('T') < l.count('V'):
        l.append('T')
for i in range(len(l)):
    print(l[i],end = '')
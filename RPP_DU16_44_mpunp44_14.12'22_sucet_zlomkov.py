vstup1 = input(f'>>>>').strip().split(' ') # citatel
vstup2 = input(f'>>>>').strip().split(' ') # menovatel
cit = vstup1[0],vstup2[0]
men = vstup1[1],vstup2[1]
cit = list(map(int,cit))
men = list(map(int, men))
print(f'{cit[0]}/{men[0]} + {cit[1]}/{men[1]} = ', end = '')
if men[0] == men[1]:    # ak su menovatele rovne
    outcit = sum(cit)   # output of citatel
    outmen = men[0]     # output od menvatel

else:                   # ak su menovatele rozdielne
    outcit = men[0]*cit[1] + men[1]*cit[0] 
    outmen = men[0]*men[1]

if outcit < outmen:     # kratenie zlomku
    div = outcit
    while outcit != 0:
        if outcit % div == 0 and outmen % div == 0:
            print(' ',int(outcit/div),'\n',int(outmen/div))
            break
        div -= 1
elif outcit > outmen:
    div = outmen
    while outcit != 0:
        if outcit % div == 0 and outmen % div == 0:
            print(' ',int(outcit/div),'\n',int(outmen/div))
            break
        div -= 1
        
else:
    print(1)
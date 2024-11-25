import random

sucet,i = 50,0
result = [100,0]

#for i in range(7):
while sucet not in result:
    i +=1
    hod = random.randrange(2)
    if hod == 0:
        sucet += -10
    else:
        sucet += 10
if sucet == 0:
    print(f'jim skoncil doma, presiel {i*10}m')
else:
    print(f'jim skoncil na poli, presiel {i*10}m')
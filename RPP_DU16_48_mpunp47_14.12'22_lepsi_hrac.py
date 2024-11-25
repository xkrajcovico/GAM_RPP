prvy = input(f'>>>>').strip().split(',')
druhy = input(f'>>>>').strip().split(',')
prvy = list(map(int,prvy))
druhy = list(map(int,druhy))
if len(prvy) > len(druhy):
    print('prvý')
elif len(prvy) < len(druhy):
    print('druhý')
else:
    if sum(prvy) > sum(druhy):
        print('prvý')
    elif sum(prvy) < sum(druhy):
        print('druhý')
    else:
        print('remíza') 
t = int(input())
# n = int(input())

def parne(intiger):
    if intiger % 2 == 0:
        return 2    # True
    else:
        return 3    # False

for i in range(t):

    total = 0
    array = input().strip().split()
    array = list(map(int,array))

    for element in array:
        total += parne(element)

    out = total / len(array)

    if out < 2.5:
        print('ANO')
    else:
        print('NE')
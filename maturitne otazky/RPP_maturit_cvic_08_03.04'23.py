t = int(input())

def absolute_value(intiger):
    if intiger >= 0:
        return intiger
    else:
        return -intiger
def bigger_lesser(intiger1,intiger2):
    if intiger1 >= intiger2:
        return intiger1
    else:
        return intiger2

for i in range(t):
    n = int(input())
    array = input().strip().split()
    array = list(map(int,array))
    i = 0
    diff = []
    while i+1 != len(array):
        diff.append(absolute_value(array[i] - array[i+1]))
        i += 1
    print(max(diff))
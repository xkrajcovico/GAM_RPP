t = int(input())

def ifint(element):
    if element.isdigit() == True:
        return int(element)
    else:
        return element

# for i in range(t):


n = int(input())
dictionary = {}
for i in range(n):
    element = input().strip().split()
    dictionary[element[0]] = element[1]
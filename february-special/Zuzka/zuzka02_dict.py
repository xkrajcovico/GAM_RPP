word = input().strip()
data = {}

for char in word:
    if char in data:
        data[char] +=1
    else:
        data[char] = 1
print(len(data))
print(*sorted(list(data.keys())))

znak = input().strip()
if znak in data:
    print(data[znak])
else:
    print('take tu neni')
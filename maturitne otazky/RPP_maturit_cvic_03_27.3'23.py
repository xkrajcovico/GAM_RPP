string_list = input().strip().split()
intiger = 0
out = [0,0,0]
print(out)
for i in range(len(string_list)):
    intiger += int(string_list[i])
for i in range(2):
    while intiger > 3600:
        intiger = intiger - 3600
        out[0] += 1
    while intiger > 60:
        intiger = intiger - 60
        out[1] += 1
    while intiger > 0:
        intiger = intiger - 1
        out[2] += 1
print(f'{out[0]} hod, {out[1]} min, {out[2]} sek')

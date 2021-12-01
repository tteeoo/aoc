l = ''
with open('input') as f:
    l = [int(x.strip()) for x in f.readlines()]

c = 0
for i,j in enumerate(l):
    try:
        if sum(l[i-4:i-1]) < sum(l[i-3:i]):
            c += 1
    except IndexError:
        pass
print(c)

l = ''
with open('input') as f:
    l = [int(x.strip()) for x in f.readlines()]

c = 0
p = l[0]
for i in l:
    if p < i:
        c += 1
    p = i
print(c)

l = []
with open('input') as f:
    l = [x.strip() for x in f.readlines()]

cb = [0] * 12
for n in l:
  for i in range(12):
    if n[i] == '0':
      cb[i] -= 1
    else:
      cb[i] += 1

g = ['0'] * 12
e = ['0'] * 12
for i in range(12):
  if cb[i] > 0:
    g[i] = '1'
  else:
    e[i] = '1'
print(''.join(g), ''.join(e))
print(int(''.join(g), 2) * int(''.join(e), 2))
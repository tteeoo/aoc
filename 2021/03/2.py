l = ''
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
  if cb[i] >= 0:
    g[i] = '1'
  else:
    e[i] = '1'

def get_o(t, cc):
  for i in range(12):
    ri = []
    for n in t:
      if cc[i] != n[i]:
        ri.append(n)
    for r in ri:
      if len(t) == 1:
        return t[0]
      t.remove(r)
  return t[1]

o = get_o(l.copy(), g)
c = get_o(l.copy(), e);

print(''.join(g), ''.join(e))
print(o, c)

print(int(o, 2) * int(c, 2))
l = []
with open('input') as f:
    l = [x.strip() for x in f.readlines()]

def get_ge(l):
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
    return (g, e)

def get_o(t, gei):
    for i in range(12):
        ri = []
        cc = get_ge(t)[gei]
        for n in t:
            if cc[i] != n[i]:
                ri.append(n)
        for r in ri:
            if len(t) == 1:
                return t[0]
            t.remove(r)
    return t[0]

o = get_o(l.copy(), 0)
c = get_o(l.copy(), 1)
print(int(o, 2) * int(c, 2))

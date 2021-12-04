l = []
with open('input') as f:
    l = [x.strip() for x in f.readlines()]

n = [int(x) for x in l[0].split(',')]
l = l[2:]
nl = []
tnl = []
for i in l:
    if i == "":
        nl.append(tnl)
        tnl = []
    else:
        tnl.append([int(x) for x in i.replace('  ', ' ').split(' ')])

def is_win(b, ns):
    for i in b:
        win = True
        for j in i:
            if j not in ns:
                win = False
        if win: return True

    for i in range(len(b[0])):
        win = True
        for j in b:
            if j[i] not in ns:
                win = False
        if win: return True

    win = True
    for i in range(5):
            if b[i][i] not in ns:
                win = False
    if win: return True

    win = True
    for i in range(4, -1, -1):
        if b[i][i] not in ns:
            win = False
    if win: return True

def usum(b, ns):
    s = 0
    for i in b:
        for j in i:
            if j not in ns:
                s += j
    return s

ww = []
won = []
for nn in range(len(n)):
    ns = n[:nn]
    for b in range(len(nl)):
        if is_win(nl[b], ns) and b not in won:
            ww.append((nn, b))
            won.append(b)

nn, b = ww[-1]
print(usum(nl[b], n[:nn]) * n[nn-1])

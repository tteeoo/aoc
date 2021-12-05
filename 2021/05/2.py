#!/usr/bin/env python3
l = []
with open('input') as f:
    l = [x.strip() for x in f.readlines()]

hls = []
vls = []
dls = []

for i in l:
    s, e = i.split(' -> ')
    li = ([int(x) for x in s.split(',')], [int(x) for x in e.split(',')])
    if li[0][0] == li[1][0]:
        vls.append(li)
    elif li[0][1] == li[1][1]:
        hls.append(li)
    else:
        dls.append(li)

mh = 0
mv = 0
for i in hls+vls+dls:
    if i[0][0] > mh:
        mh = i[0][0]
    if i[1][0] > mh:
        mh = i[1][0]
    if i[0][1] > mv:
        mv = i[0][1]
    if i[1][1] > mv:
        mv = i[1][1]

g = []
for _ in range(mv+1):
    g.append([0 for _ in range(mh+1)])

for i in hls:
    r = sorted((i[0][0], i[1][0]))
    for j in range(r[0], r[1]+1):
        g[i[0][1]][j] += 1
for i in vls:
    r = sorted((i[0][1], i[1][1]))
    for j in range(r[0], r[1]+1):
        g[j][i[0][0]] += 1
for i in dls:
    r = sorted((i[0][0], i[1][0]))
    for j in range(r[1]-r[0]+1):
        hc = 1
        vc = 1
        if i[0][0] > i[1][0]:
            hc = -1
        if i[0][1] > i[1][1]:
            vc = -1
        g[i[0][1]+(j*vc)][i[0][0]+(j*hc)] += 1

c = 0
for i in g:
    for j in i:
        if j > 1:
            c += 1
print(c) 

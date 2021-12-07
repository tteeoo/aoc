#!/usr/bin/env python3
l = ''
with open('input') as f:
    l = [int(x) for x in f.read().split(',')]

minf = -1
for i in range(max(l)):
    s = 0 
    for j in l:
        s += sum(range(1, abs(i - j)+1))
    if s < minf or minf == -1:
        minf = s
print(minf)

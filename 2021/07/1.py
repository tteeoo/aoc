#!/usr/bin/env python3
l = ''
with open('input') as f:
    l = [int(x) for x in f.read().split(',')]

s = sorted(l)[len(l)//2]
d = 0
for i in l:
    d += abs(s - i)
print(d)

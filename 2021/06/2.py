#!/usr/bin/env python3
l = []
with open('input') as f:
    l = [int(x) for x in f.read().strip().split(',')]

f = [0 for _ in range(9)]
for i in l:
  f[i] += 1

for i in range(256):
  old = f[0]
  for j in range(len(f)):
    if j == 8:
      f[j] = old
    elif j == 6:
      f[j] = f[j+1] + old
    else:
      f[j] = f[j+1]
print(sum(f))
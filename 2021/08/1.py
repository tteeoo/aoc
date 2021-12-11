#!/usr/bin/env python3
l = []
with open('input') as f:
    l = [[x.split(' '), y.split(' ')] for x, y in [
      x.strip().split(' | ') for x in f.readlines()]]

c = 0
for i in l:
  for j in i[1]:
    if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
      c += 1
print(c)
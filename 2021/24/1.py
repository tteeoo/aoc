#!/usr/bin/env python3
import math
l = []
with open('input') as f:
    l = [x.strip() for x in f.readlines()]

var = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

def inp(v, i):
    var[v] = i

def add(v1, v2):
    try:
        var[v1] += int(v2)
    except:
        var[v1] += var[v2]

def mul(v1, v2):
    try:
        var[v1] *= int(v2)
    except:
        var[v1] *= var[v2]

def div(v1, v2):
    try:
        var[v1] = math.floor(var[v1] / int(v2))
    except:
        var[v1] = math.floor(var[v1] / var[v2])

def mod(v1, v2):
    try:
        var[v1] %= int(v2)
    except:
        var[v1] %= var[v2]

def eql(v1, v2):
    try:
        if var[v1] == int(v2):
            var[v1] = 1
        else:
            var[v1] = 0
    except:
        if var[v1] == var[v2]:
            var[v1] = 1
        else:
            var[v1] = 0

for op in l:
    op = op.split(' ')
    if op[0] == 'inp':
        print(var['z'])
        exec(op[0] + '("' + op[1] + '",' + input() + ')')
    else:
        exec(op[0] + '("' + '","'.join(op[1:]) + '")')

print(var)

#!/usr/bin/env python3
import math

def monad(z, w, b, c):
    if b < 0:
        z = math.floor(z / 26)
    if w != (z % 26 + b):
        z = 26 * z + w + c
    return z

if __name__ == '__main__':
    z = 0
    for b, c in [(15 , 15),
            (12, 5),
            (13, 6),
            (-14, 7),
            (15, 9),
            (-7, 6),
            (14, 14),
            (15, 3),
            (15, 1),
            (-7, 3),
            (-8, 4),
            (-7, 6),
            (-5, 7),
            (-10, 1)]:
        z = monad(z, int(input()), b, c) 
        print(z)

#!/bin/sh
curl "https://adventofcode.com/2021/day/$1/input" -b "session=$2" > input

l = ''
with open('input') as f:
    l = [x.strip() for x in f.readlines()]

x = 0
y = 0
a = 0
for i in l:
  s = i.split()
  if s[0] == "forward":
    x += int(s[1])
    y += a * int(s[1])
  if s[0] == "up":
    a -= int(s[1])
  if s[0] == "down":
    a += int(s[1])
print(x * y)
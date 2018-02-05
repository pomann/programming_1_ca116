import sys

n = int(sys.argv[1])
f = raw_input()
m = []
i = 0

while f != "end":
  m.append(f)
  i += 1
  f = raw_input()

if n > i:
  o = 0
else:
  o = i - n


while o < i:
  print m[o]
  o += 1

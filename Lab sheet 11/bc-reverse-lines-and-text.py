n = raw_input()
m = []
p = ""
i = 0
a = 0

while n != "end":
  m.append(n)
  n = raw_input()

while i < len(m):
  o = 1
  while o <= len(m[a]):
     p = p + m[a][len(m[a]) - o]
     o += 1
  a += 1
  i += 1
  print (p)
  p = ""


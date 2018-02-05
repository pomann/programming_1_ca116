import sys
n = int(sys.argv[1])
s = 2

while s < n:
  i = 2
  while i * i <= s and s % i != 0:
     i += 1

  if i * i <= s:
     True
  else:
     print s
  s = s + 1

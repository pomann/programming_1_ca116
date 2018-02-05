import sys

n = sys.argv[1]
i = len(n) - 1
o = ''

while i >= 0:
	o = o + n[i]
	i = i - 1

print o


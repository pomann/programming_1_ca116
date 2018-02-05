import sys

n = sys.argv[1]
o = ''
i = 1

o = o + n[0]

while i < len(n):
	if n[i] != n[i - 1]:
		o = o + n[i]
	i = i + 1

print o

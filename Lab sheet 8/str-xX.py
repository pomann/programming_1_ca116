import sys

n = sys.argv[1]
o = ''
i = 0

while i < len(n):
	if n[i].islower():
		o = o + 'x'
	elif n[i].isupper():
		o = o + 'X'
	else:
		o = o + n[i]
	i = i + 1

print o

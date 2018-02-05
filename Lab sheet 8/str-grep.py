import sys

l = sys.argv[1]
n = raw_input()
a = []
i = 0


while n != 'end':
	if l in n:
		a.append(n)
	n = raw_input()

for m in a:
	print m

import sys

l = int(sys.argv[1])
n = raw_input()
a = []

while n != 'end':
	a.append(n)
	n = raw_input()

for m in a:
	print ' ' * ((l - len(m)) / 2) + str(m)

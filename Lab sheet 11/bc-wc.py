import sys

l = sys.argv[1]
n = raw_input()
a = []
i = 0


while n != 'end':
	if l in n:
		i = i + 1
	n = raw_input()

print i

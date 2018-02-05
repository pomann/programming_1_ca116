import sys
n = sys.argv[1:]
c = 0
tbp = 0
difference = 0

for i in n:
	if len(i) > c:
		c = len(i)


tbp = c + 4

print "*" * tbp

for i in n:
	if len(i) < c:
		difference = c - len(i)
		print "*", i, " " * difference + "*"
	else:
		print "*", i, "*"

print "*" * tbp

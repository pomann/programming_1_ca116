import sys

n = int(sys.argv[1])
i = 0
total = 0

while total < n:
	total = 2 ** i
	if total < n:
		print total
	i = i + 1

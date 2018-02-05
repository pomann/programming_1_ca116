import sys

n = int(sys.argv[1])
i = 0
total = 0

while total < n:
	total = i * 2
	if total < n:
		print total
	i = i + 1

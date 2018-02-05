n = raw_input()
i = 0
d = ""

while i < len(n):
	if i % 2 == 0:
		d = d + n[i]
	i += 1

print d

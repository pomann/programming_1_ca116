n = raw_input()
i = 0
k = ""

while i < len(n):
	if n[i].isspace():
		i = i
	else:
		k = k + n[i]
	i = i + 1

print k

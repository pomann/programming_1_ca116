lines = []
n = raw_input()

while n != 'end':
	if n not in lines:
		lines.append(n)
	n = raw_input()

print lines

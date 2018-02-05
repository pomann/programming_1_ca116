lines = []
n = raw_input()
i = 1

while n != 'end':
	if n not in lines:
		lines.append(int(n))
	n = raw_input()

lines.sort()

for i in lines:
	print i

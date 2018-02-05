lines = []
n = raw_input()

while n != 'end':
	lines.append(int(n))
	n = raw_input()

for i in lines:
	if i % 2 == 0:
		print i

for i in lines:
	if i % 2 != 0:
		print i

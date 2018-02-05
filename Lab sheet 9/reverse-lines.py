lines = []
n = raw_input()
i = 0

while n != 'end':
	lines.append(n)
	n = raw_input()

while i < len(lines):
	print lines.pop()

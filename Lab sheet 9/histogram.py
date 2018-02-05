no = []
n = raw_input()
i = 0

while n != 'end':
	no.append(int(n))
	n = raw_input()

while i < 10:
	i2 = 0
	count = 0
	while i2 < len(no):
		if no[i2] == i:
			count = count + 1
		i2 = i2 + 1
	print i, '*' * count
	count = 0
	i = i + 1

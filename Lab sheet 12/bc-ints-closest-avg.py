n = raw_input()
maxim = 0.0
i = 0
a = []
b = []

while n != 'end':
	maxim = maxim + float(n)
	i = i + 1
	a.append(float(n))
	n = raw_input()

if i != 0:
	maxim = maxim / i

	i2 = 0
	while i2 < len(a):
		b.append(a[i2] - maxim)
		i2 = i2 + 1

	low = 0
	if b[0] < 0:
		low = b[0] * (-1)
	else:
		low = b[0]

	index = 0
	i3 = 0
	while i3 < len(b):
		if b[i3] < 0:
			b[i3] = b[i3] * (-1)
			if b[i3] < low:
				low = b[i3]
				index = i3
		else:
			if b[i3] < low:
				low = b[i3]
				index = i3
		i3 = i3 + 1
	
	print int(a[index])
else:
	print i

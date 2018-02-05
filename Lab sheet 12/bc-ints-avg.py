n = raw_input()
maxim = 0
i = 0

while n != 'end':
	maxim = maxim + int(n)
	i = i + 1
	n = raw_input()

if i == 0:
	print maxim
else:
	print maxim / i

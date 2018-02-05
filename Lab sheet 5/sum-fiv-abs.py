i = 0
total = 0

while i < 5:
	n = input()
	if n > 0:
		total = total + n
	else:
		n = n * (-1)
		total = total + n
	i = i + 1

print total

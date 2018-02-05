i = 0
total = 0
total_1 = 0

while i < 5:
	n = input()
	if n > 0:
		total = total + n
	else:
		total_1 = total_1 + n
	i = i + 1

print total_1, total

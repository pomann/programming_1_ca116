a = input()
b = input()
i = 0
t = 0

while t < a:
	t = b ** i
	i = i + 1

i = i - 2

while i >= 0:
	print a / (b ** i)
	a = a % (b ** i)
	i = i - 1



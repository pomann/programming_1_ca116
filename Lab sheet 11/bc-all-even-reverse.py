import sys

l = raw_input() 
a = []
i = 0

while l != 'end':
	a.append(int(l))
	i = i + 1
	l = raw_input() 

i2 = len(a) - 1
while i2 >= 0:
	if a[i2] % 2 == 0:
		print a[i2]
	i2 = i2 - 1

n = raw_input()
a = []
maxim = 0
maxim = int(n)

while n != 'end':
	if int(n) > maxim:
		maxim = int(n)
	a.append(int(n))
	n = raw_input()

if len(a) == 0:
	print '0'
else:
	print maxim 

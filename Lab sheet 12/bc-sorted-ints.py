n = raw_input()
a = []

while n != 'end':
	a.append(int(n))
	n = raw_input()

i = 1
while i < len(a):
	if a[i] < a[i - 1]:
		print 'not sorted'
		break
	i = i + 1
	if i == len(a):
		print 'sorted'

if not a or len(a) == 1:
	print 'sorted'

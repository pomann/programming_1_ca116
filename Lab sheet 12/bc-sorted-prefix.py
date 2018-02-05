n = raw_input()
a = []

while n != 'end':
	a.append(int(n))
	n = raw_input()

i = 1
while i < len(a):
	if a[i] < a[i - 1]:
		for l in a[0:i]:
			print l
		break
	i = i + 1

if len(a) == 1:
	print a[0] 

if i == len(a) and len(a) != 1:
	for l in a:
		print l

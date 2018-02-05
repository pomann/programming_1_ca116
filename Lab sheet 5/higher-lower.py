a = input()
i = 0

while i < 5:
	n = input()
	if a < n:
		print 'higher'
	elif a > n:
		print 'lower'
	else:
		print 'equal'
	i = i + 1
	a = n

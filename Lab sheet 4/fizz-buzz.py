n = input('Enter n: ')
i = 1

while i <= n:
	if i % 3 == 0 and i % 5 == 0:
		print 'Fizz Buzz'
	elif i % 3 == 0:
		print 'Fizz'
	elif i % 5 == 0:
		print 'Buzz'
	else:
		print i
	i = i + 1

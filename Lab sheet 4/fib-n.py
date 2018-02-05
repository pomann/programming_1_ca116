n = input('Enter n: ')
p = 0
c = 1
tmp = 0
i = 0

print c

while i < n - 1:
	print p + c
	tmp = c
	c = p + c
	p = tmp
   	i = i + 1

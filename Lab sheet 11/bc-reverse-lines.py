n = raw_input()
c = len(n) - 1
t = []


while n != 'end':
	t.append(n)
	n = raw_input()

i = len(t) - 1

while i >= 0:
	print t[i]
	i = i - 1

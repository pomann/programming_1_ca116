m = 'AEIOU'
n = raw_input()
a = []
i = 0


while n != 'end':
	for l in n:
		for k in l:
			for b in m:
				if b == k:
					a.append(n)
					break
	n = raw_input()

for m in a:
	print m

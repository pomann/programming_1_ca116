n = raw_input()
i = 0

while i < (len(n) / 2): 
	if n[i] == n[len(n) - 1 - i]:
		i = i + 1
	else:
		break

if i == (len(n) / 2):
	print n

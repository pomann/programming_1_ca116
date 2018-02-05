n = raw_input()
c = len(n) - 1
t = ""

while 0 <= c:
	t = t + n[c]
	c = c - 1

print t

import sys
n = str(sys.argv[1])
l = []
l.append(n)
i = 0
num = 0

while i < 10:
	if l[i] == l[i][::-1]:
		print l[i][::-1]
		break
	else:
		num = int(l[i]) + int(l[i][::-1])
		l.append(str(num))
	i += 1
	if i == 10:
		print "none", num

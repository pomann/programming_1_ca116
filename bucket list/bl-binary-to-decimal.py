import sys
n = sys.argv[1]
i = len(n) - 1
dec = 0

for l in n:
	dec = dec + (int(l) * 2 ** i)
	i = i - 1
	
print (dec)

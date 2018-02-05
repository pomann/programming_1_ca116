import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   	line = lines[i]
   	details = line.split()
	print ' '.join(details[0:5]), ''.join(details[len(details) - 1]) + ',', ' '.join(details[5:len(details) - 1])
   	i = i + 1

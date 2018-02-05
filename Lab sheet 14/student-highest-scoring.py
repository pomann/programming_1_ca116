import sys

lines = sys.stdin.readlines()
highest = 0
name = '' 

i = 0
while i < len(lines):
   	line = lines[i]
   	details = line.split()
   	if details[4] > highest:
		highest = details[4]
		name = ' '.join(details[5:])
   	i = i + 1

if i != 0:
	print name

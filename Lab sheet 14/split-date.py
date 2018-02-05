import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   	line = lines[i]
	line = line.strip()
   	details = line.split('/')
   	for l in details:
		print l
   	i = i + 1


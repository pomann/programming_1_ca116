import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   if ' '.join(details[1:3]) == 'BBC News':
	print ' '.join(details[:])
   i = i + 1

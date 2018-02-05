import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   	line = lines[i]
   	details = line.split()
   	print details[4]
   	i = i + 1


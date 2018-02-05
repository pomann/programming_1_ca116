import sys

lines = sys.stdin.readlines()
total = 0.0

i = 0
while i < len(lines):
   	line = lines[i]
   	details = line.split()
   	total = total + float(details[4])
   	i = i + 1

if i == 0:
	print total
else:
	print total / i

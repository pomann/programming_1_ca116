import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   	line = lines[i]
   	details = line.split()
   	if int(details[4]) >= 70:
		print ' '.join(details[0:5]), '1', ' '.join(details[5:])
	elif int(details[4]) >= 60:
		print ' '.join(details[0:5]), '2.1', ' '.join(details[5:])
	elif int(details[4]) >= 50:
		print ' '.join(details[0:5]), '2.2', ' '.join(details[5:])
	elif int(details[4]) >= 40:
		print ' '.join(details[0:5]), '3', ' '.join(details[5:])
	else: 
		print ' '.join(details[0:5]), 'F', ' '.join(details[5:])
   	i = i + 1


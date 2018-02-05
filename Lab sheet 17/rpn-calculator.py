print "!!! Type 'quit' to end the program !!!"
n = raw_input('Enter an expression: ')

out = 0
while n != 'quit':
	n = n.split()
	i = 0
	if len(n) > 3:
		while i < len(n):
			if n[i].isdigit():
				i = i
			else:
				if n[i] == '+':
					n[i - 2] = int(n[i - 2]) + int(n[i - 1])
					n.remove(n[i])
					n.remove(n[i - 1])
		
				elif n[i] == '-':
					n[i - 2] = int(n[i - 2]) - int(n[i - 1])
					n.remove(n[i])
					n.remove(n[i - 1])
	
				elif n[i] == '*':
					n[i - 2] = int(n[i - 2]) * int(n[i - 1])
					n.remove(n[i])
					n.remove(n[i - 1])
			
				elif n[i] == '/':
					n[i - 2] = int(n[i - 2]) / int(n[i - 1])
					n.remove(n[i])
					n.remove(n[i - 1])
	
				elif n[i] == '**':
					n[i - 2] = int(n[i - 2]) ** int(n[i - 1])
					n.remove(n[i])
					n.remove(n[i - 1])
	
			i = i + 1

	if n[2] == '+':
		print int(n[0]) + int(n[1])
				
	elif n[2] == '-':
		print int(n[0]) - int(n[1])
			
	elif n[2] == '*':
		print int(n[0]) * int(n[1])
					
	elif n[2] == '/':
		print int(n[0]) / int(n[1])
				
	elif n[2] == '**':
		print int(n[0]) ** int(n[1])

	n = raw_input('Enter an expression: ')
			

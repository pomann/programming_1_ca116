import getpass			#imports passwords

n = list(getpass.getpass('Word to be guessed:')) #hides input
		
i = 0
g = ''
seen = []

while i < len(n):					#Converts words into _
	if n[i].isupper() or n[i].islower():
		g = g + '_'
	else:
		g = g + n[i]
	i = i + 1

g = list(g)						#Converts _ into list

wrong = input('Enter no. of lives: ')

i2 = 0
while n != g:
	print ''.join(g)
	m = raw_input('guess: ')

	if m in seen:		#If letter already guessed prints warning
		print '!! You have already guessed this letter !!'
	
	
	i3 = 0
	while i3 < len(n):					#If guess correct swaps _ for letter
		if n[i3] == m.lower() or n[i3] == m.upper():
			g[i3] = n[i3]
		i3 = i3 + 1

	if m not in n:
		if m not in seen:			#wrong guests counter
			i2 = i2 + 1
			print 'Lives:', wrong - i2
	seen.append(m)

	if i2 == wrong:			#if limit is reached you lost
		break

if n == g:			#Prints win/lost message
	print 'You Win:', ''.join(n)
else:
	print 'You Lost:', ''.join(n)


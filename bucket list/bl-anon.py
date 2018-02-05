import sys

lines = sys.stdin.readlines()
seen = []
counter = 0
i = 0


while i < len(lines):
	line = lines[i]
	details = line.split()
	l = 0
	while l < len(seen) and seen[l] != details[3]:
		l += 1
	have_seen = l < len(seen)

	if not have_seen:
		seen.append(details[3])
	
	p = 0
	while p < len(seen):
		if details[3] == seen[p]:
			print (" ".join(details[:3]),"user-"+str(p + 1), " ".join(details[4:]))
		p += 1
	i += 1

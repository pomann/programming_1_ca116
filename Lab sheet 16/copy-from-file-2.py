import sys
n = sys.argv[1]


with open(n , "r") as f:
  for line in f.readlines():
     sys.stdout.write(line)

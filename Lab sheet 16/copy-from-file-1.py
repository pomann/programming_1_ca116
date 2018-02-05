import sys


with open("translation.txt" , "r") as f:
  for line in f.readlines():
     sys.stdout.write(line)

import sys
l = sys.argv[1]
m = ""

n = {
  "one": "eins",
  "two": "zwei",
  "three": "drei",
  "four": "vier",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eigth": "acht",
  "nine": "neun",
  "ten": "zehn",
}

for key in n:
  if key == l:
     m = n[key]

print "The German for", l ,"is",m+"."

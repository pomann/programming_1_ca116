n = raw_input()
a = []
i = 0
o = 1
p = 0

while n != "end":
  a.append(int(n))
  o += 1
  p +=1
  n = raw_input()

while i < len(a):
  p = i             
  j = i + 1         
  while j < len(a):  
     if a[j] < a[p]: 
        p = j        
     j = j + 1       

  tmp = a[p]         
  a[p] = a[i]        
  a[i] = tmp         

  i = i + 1

if o % 2 == 0:
  print a[(o / 2) - 1]
else:
  print a[(p / 2) + 1]

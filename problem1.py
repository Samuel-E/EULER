def multcalc (y):
  x=0
  z=0
  while x < y:
    if x % 3 == 0 or x % 5 == 0:
      z += x
      x+=1
    else:
      x+=1

    
  print(z)
  return z  

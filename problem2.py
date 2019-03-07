def FibEvenSum (limit):
  x = 1
  y = 2
  z = x + y
  total = 2
  while z < limit:
    if z % 2 == 0:
      total += z
      x = y
      y = z
      z = x + y
    else:
      x = y
      y = z
      z = x + y
  
  print(total)
  return total

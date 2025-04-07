def triangle(n):
  if n == 1:
    return "*\n"
  
  res = "*\n" 
  for i in range(1, n):
    if i % 2 != 0:
      num = (i + 1) // 2
      res += " *" * num + "\n"
    else:
      num = i // 2
      res += "* " * num + "*\n"
  
  return res

print(triangle(1))
print(triangle(4))
print(triangle(5))
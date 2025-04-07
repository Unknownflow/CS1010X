def interleaved_tuple(tuple_a, tuple_b):
  ptr = 0
  res = ()

  while ptr < len(tuple_a):
    res += (tuple_a[ptr], tuple_b[ptr])
    ptr += 1
  
  return res

print(interleaved_tuple((1,3,5,7,9),(2,4,6,8,10)))
print(interleaved_tuple((2,4,6,8,10),(1,3,5,7,9)))
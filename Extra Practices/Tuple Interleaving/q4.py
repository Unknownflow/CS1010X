def interleaved_tuple_picky(tuple_a, tuple_b, predicate):
  res = ()

  for i in range(len(tuple_a)):
    if predicate(tuple_a[i]):
      res += (tuple_a[i], )
    else:
      res += (tuple_b[i], )
  
  return res

is_odd = lambda x: x % 2 == 1
print(interleaved_tuple_picky((1, 2, 3, 4, 5), (9, 11, 13, 15, 17), is_odd))
print(interleaved_tuple_picky((10, 11, 12, 13, 14), (1, 2, 3, 4, 5), is_odd))
print(interleaved_tuple_picky((1, 1, 1, 1, 1), (2, 3, 4, 5, 6), is_odd))
print(interleaved_tuple_picky((2, 2, 2, 2, 2), (3, 4, 5, 6, 7), is_odd))
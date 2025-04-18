def make_stack():
  stack = []
  def helper(command, *args):
    if command == "push":
      stack.append(args[0])
      return None
    elif command == "size":
      return len(stack)
    elif command == "peek":
      return stack[-1]
    elif command == "pop":
      popped = stack.pop()
      return popped
  return helper

def prefix_infix(lst):
    stack = make_stack()
    res = ""

    for items in lst:
      if type(items) == list:
        count = 0
        while True: 
          stack("push", items[0])
          res += "("
          count += 1
          if type(items[1]) != list:
            break
          items = items[1]
        
        op = stack("pop")
        res += str(items[1]) + op + str(items[2])
        for i in range(count):
          res += ")"

      else:          
        stack("push", items)
        res += "("
    return res

print(prefix_infix (['+', ['*', 5, 4], ['-', 2, 1]]))

print(prefix_infix(['-',['*',5,4],['-',['/',1,45],['+',1,1]]]))
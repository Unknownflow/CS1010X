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

stk = make_stack()
print(stk("push", 1))
print(stk("push", 2))
print(stk("push", 3))
print(stk("peek"))
print(stk("pop"))
print(stk("peek"))
print(stk("size"))
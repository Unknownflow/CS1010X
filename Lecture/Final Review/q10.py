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


def prefix_infix(expr):
    stack = make_stack()
    frame_stack = make_stack()  # simulate call stack: (expr, visited_flag)

    frame_stack("push", (expr, False))

    while frame_stack("size") > 0:
        node, visited = frame_stack("pop")

        if isinstance(node, list):
            if visited:
                # Process operator node after children are on the stack
                right = stack("pop")
                left = stack("pop")
                operator = node[0]
                stack("push", f"({left} {operator} {right})")
            else:
                # Post-order: push current node again as visited, then right, then left
                frame_stack("push", (node, True))        # revisit this node
                frame_stack("push", (node[2], False))    # right child
                frame_stack("push", (node[1], False))    # left child
        else:
            # Operand: just push as string
            stack("push", str(node))

    return stack("pop")


def prefix_infix(expr):
    stack = make_stack()

    for op in expr:
        if op in ["*", "/", "+", "-"]:
            stack("push", str(op))
        elif stack("peek") in ["*", "/", "+", "-"]:
            stack("push", str(op))
        else:
            tmp = "(" + stack("pop") + stack("pop") + str(op) + ")"
            while stack("size") > 0 and stack("peek") not in ["*", "/", "+", "-"]:
                tmp = "(" + stack("pop") + stack("pop") + tmp + ")"
            stack("push", tmp)

    while stack("size") > 1:
        back = stack("pop")
        front = stack("pop")
        stack("push", "(" + front + stack("pop") + back + ")")

    return stack("pop")


print(prefix_infix(['+', ['*', 5, 4], ['-', 2, 1]]))

print(prefix_infix(['-', ['*', 5, 4], ['-', ['/', 1, 45], ['+', 1, 1]]]))

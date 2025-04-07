def untuplify(tpl):
    if len(tpl) == 1:
        return int(tpl[0])
    else:
        return int(tpl[0]) * (10**(len(tpl)-1)) + untuplify(tpl[1:])

print(untuplify((1, 2, 3, 4, 5)))
print(untuplify((1, 0, 2, 4, 8, 6)))
print(untuplify((1, 0)))

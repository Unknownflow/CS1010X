

# easiest question
def make_mtf():
    stuff = []  #
    movement_count = [0]   # cannot use simply 0, must be a lis - or need to declare nonlocal stuff
    def helper(op, *arg):
        if op=="append":  
            stuff.append(arg[0])
        elif op=="list":
            return (stuff)
        elif op=="is_empty":  
            return stuff == []
        elif op=="clear":
            stuff.clear() # wrong to put stuff=[] as it will become local variable - then need to declare nonlocal, I think
        elif op=="find":
            if arg[0] in stuff:
                found = stuff.index(arg[0])
                stuff.remove(arg[0])
                stuff.insert(0,arg[0])
                movement_count[0] += found
                return found
            else:
                return -1
        elif op=="remove":
            if arg[0] in stuff:
                stuff.remove(arg[0])
        elif op=="movement":
            return (movement_count[0])
        else:
            return("error msg")
    return helper

m = make_mtf()
m("append",3)
m("append", 5)
m("append", 55)
m("append", 66)
print(m("list"))                # Ans: [3, 5, 55, 66]
print(m("find", 55))      # Ans: 2
print(m("list"))                # Ans: [55, 3, 5, 66]
print(m("movement"))             # Ans: 2
print(m("find", 66))      # Ans: 3
print(m("list"))                # Ans: [66, 55, 3, 5]
print(m("find", 56))      # Ans: -1
m("remove", 5)            # 5 in m is removed
m("remove", 56)           # No change to m
print(m("list"))                # Ans: [66, 55, 3]
print(m("movement"))             # Ans: 5







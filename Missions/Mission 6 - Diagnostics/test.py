def copy_tree(tree):
    def tree_map(fn, tree):
        def mapping_fn(subtree):
            if type(subtree) != tuple:
                return fn(subtree)
            else:
                return tree_map(fn, subtree)
        return tuple(map(mapping_fn, tree))
    
    return tree_map(lambda x: x, tree)

# Do not remove this line
original = (1, 2, 3, 4)


print(copy_tree(original))

x = (1, 2, (3, 4))
y = copy_tree(x)
print(y)
print(y is x)

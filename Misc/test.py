def house_of_cards(h):
    if h == 1:
        return 1
    if h == 2:
        return 5
        
    
    return 2 * house_of_cards(h-1) - house_of_cards(h-2) + h + 1

for i in range(1,10):
    print(house_of_cards(i))


def num_triangles(h):
    if h == 1:
        return 0
    else:
        num = 0 # undercounted triangles

        # undercounted upright triangle
        for i in range(1, h):
            num += i
        
        # undercounted inverted triangle
        for i in range(h-1, 0, -2):
            num += i
        
        return num + num_triangles(h-1)

for i in range(1, 10):
    print(num_triangles(i))

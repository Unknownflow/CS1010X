# Rabbit Jump

# A bunny can hop at most 50 centimetres far. It wants to cross to the other side of the river, but it cannot swim. So the only hope is to hop on the rocks on the river, which are positioned in a straight line. The positions of the rocks are measured from the start location, assuming that the bunny starts at the 0 cm mark. The opposite bank could be treated as a big rock. It is the final rock in the tuple of rocks.

# In the Figure below, the rocks are at locations 32, 46, 70, 85, 96, 123, and the opposite riverbank at location 145.

# The bunny will jump as far as it could for each hop. What is the smallest number of jumps it needs to take to reach the other side of the river? For the above example, it needs to make 3 jumps, as shown in the diagram above.

# You may assume that there are at most 20 rocks (including the opposite bank).

# Write a function rabbit that reads in a tuple that represents the locations of the rocks. Your function should return the minimum number of jumps needed, or -1 if it is not possible for the bunny to reach the other side of the river. You may assume that the locations of the rocks in the tuple are valid (bigger than 0) and they are sorted in ascending order.

def rabbit(rocks):
    max_hop = 50
    prev_hop = 0
    prev_pos = 0
    prev_jump_pos = 0
    jumps = 0
    reached = False
    
    for rock in rocks:
        hop_dist = rock - prev_jump_pos

        print(rock, hop_dist, prev_hop, prev_jump_pos)
        if hop_dist > max_hop:
            if prev_hop != 0:
                prev_hop = 0
                prev_jump_pos = prev_pos
                jumps += 1
                print(jumps)
        else:
            if rock == rocks[-1] and rock - prev_pos <= max_hop:
                jumps += 1
                reached = True
            prev_hop = hop_dist

        prev_pos = rock

    if not reached:
        return -1
    return jumps


# print(rabbit((32, 46, 70, 85, 96, 123, 145))) # 3
# print(rabbit((40, 70, 150, 160, 180))) # -1
print(rabbit((30, 70, 75, 120, 160, 170, 180, 190, 200, 246, 258))) # 7
# print(rabbit((51, 52, 53, 54, 55, 56, 57, 58))) # -1
# print(rabbit((50, 51, 101, 102, 152, 153, 203, 204, 254, 255, 305, 306, 356, 357, 407))) # 15        

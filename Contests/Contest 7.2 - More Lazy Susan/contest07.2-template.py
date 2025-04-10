#
# CS1010X --- Programming Methodology
#
# Contest 7.2 Template

from more_lazy_susan import *

def create_solver(coins):
    # insert your code here    
    def solver(move_id):
        # insert your code here
        idx_to_flip = [False] * coins

        # # Use a block flipping pattern based on move_id.
        # if coins == 13:
        #     # For 13 coins, let's try flipping coins in a sequence that mimics blocks:
        #     # Example: For each move_id, flip a block of coins in varying sizes
        #     block_size = (move_id % 6) + 1  # This creates a variety of block sizes from 1 to 7
            
        #     # Flip coins in a block pattern (block_size depends on move_id % block_size)
        #     for i in range(coins):
        #         if (i + move_id) % block_size == 0:
        #             idx_to_flip[i] = True

        # elif coins == 15:
        #     # For 15 coins, use a different block pattern, for example, using a larger block size
        #     block_size = (move_id % 7) + 2  # This creates a variety of block sizes from 2 to 6

        #     # Flip coins in a block pattern (block_size depends on move_id % block_size)
        #     for i in range(coins):
        #         if (i + move_id) % block_size == 0:
        #             idx_to_flip[i] = True
        
        # else:
            # cyclic flipping
        for i in range(coins):
            if (i + move_id) % coins == 0:
                idx_to_flip[i] = True

        return tuple(idx_to_flip)
    
    return solver


# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
get_contest_score(create_solver, True)

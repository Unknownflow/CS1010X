# Elevator

# Suppose you are to operate two elevators. Implement a function operate_elevator that reads two tuples of operation instructions and moves elevators according to the instructions.

# The two elevators are both initially positioned at level 1 and it take 2 seconds for an elevator to move one level up or down. Each tuple operates on one elevator only and contains 3 integers, e.g. (1, 3, 6)

# The meaning of each integer in the above instruction is as follows:

#     First number (elevator number, either 1 or 2) indicates one of the two elevators to operate on.

#     Second number (from level) indicates which level a passenger presses the button of that elevator. The elevator would have to travel from where it currently is to that level to pick up that person. In case that a passenger happens to be at the same level where an elevator is currently at, it is natural that the elevator does not need to move up/down in order to pick up that passenger.

#     Third number (to level) indicates which level a passenger wants to go. You can assume that the from level is always different from to level and therefore, no input validation is needed.

# For example, let’s assume that elevator 1 is currently at level 1 and the first instruction is 1 3 6. Hence elevator 1 has to move from level 1 to level 3 to pick up the passenger first and then moves to level 6 where the passenger will alight. In brief, elevator 1 takes (2+3)*2 seconds to finish movement and ends at level 6 (an elevator will stop at to level and never move without a further instruction).

# As another example, assume that the second instruction is 2 6 2 and elevator 2 is currently at level 1. Hence elevator 2 will move upward to level 6 to pick up a passenger first and then move down to level 2 to let the passenger alight. In total, it takes (5+4)*2 seconds to finish movement and stops at level 2.

# Your program is to read two instructions one by one and print out the time taken for each elevator to move and the final position of each elevator. Take note of the case that two instructions may operate on the same elevator.

# Define the elevator speed (2 seconds per level) as a constant in your program.

# The output should be a tuple of tuples with the following format (<elevator_num>, <time_taken>, <final_floor>), with the first tuple for elevator 1 and the second tuple for elevator 2.

ELEVATOR_SPEED = 2

def operate_elevator(t1, t2):

    elevator_one_level = 1

    elevator_two_level = 1

    elevator_one_time = 0

    elevator_two_time = 0

    for instruction in (t1, t2):

        elevator_num, from_level, to_level = instruction

        distance = 0

        if elevator_num == 1:

            distance += abs(from_level - elevator_one_level)

            distance += abs(to_level - from_level)

            elevator_one_level = to_level

            elevator_one_time += distance * ELEVATOR_SPEED

        else:

            distance += abs(from_level - elevator_two_level)

            distance += abs(to_level - from_level)

            elevator_two_level = to_level

            elevator_two_time += distance * ELEVATOR_SPEED

                    

    return ((1, elevator_one_time, elevator_one_level), (2, elevator_two_time, elevator_two_level))
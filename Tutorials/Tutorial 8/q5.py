def make_monte_carlo_integral(P,x1,y1,x2,y2):
    num_trials = 0
    estimate = 0

    def helper(command, *args):
        
        if command == "run_trials":
            num_trials += args
            P(x1, y1)
            P(x2, y2)
            return None
        elif command == "trials":
            return num_trials
        elif command == "get estimate":
            return estimate
    
    return helper

### DO NOT MODIFY THIS ###
import math
import random

def circle(x,y):
    return math.sqrt(x*x+y*y) < 1

circle_estimate = make_monte_carlo_integral(circle,-1,-1,1,1)

print(circle_estimate("run trials", 1000))
print(circle_estimate("trials"))
### The inrange function in testcases is used to check whether a value lies in a specified range.

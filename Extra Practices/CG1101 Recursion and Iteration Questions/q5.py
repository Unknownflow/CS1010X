#Question 5

#Conway Sequence

#The Conway’s recursive sequence is defined by the following recurrence relation for any positive integer n.

def conway(n):

    # code that implements Conway's recursive sequence.

    if n == 1 or n == 2:

        return 1

    else:

        return conway(conway(n-1)) + conway(n-conway(n-1))

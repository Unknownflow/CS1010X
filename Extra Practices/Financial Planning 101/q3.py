#Question 3

#Deferred Annuity

#A deferred annuity is an annuity which delays its payouts. This means that the payouts do not start until after a certain duration. Notice that a deferred annuity is just a deposit at the start, followed by an annuity. Your task is to define a Higher-order Function that returns a function that takes in a given interest rate and outputs the amount of money that is left in a deferred annuity. You may assume that deposit and balance have been defined for you.

#Define a function new_balance(principal, gap, payout, duration) that returns a single-parameter function which takes in a monthly interest rate and outputs the balance in a deferred annuity. gap is the duration in months before the first payment, payout is monthly and duration is just the total number of payouts.

def new_balance(principal, gap, payout, duration):

    def balance(principal, interest, payout, duration):

        if duration == 0:

            return principal / (1 + interest)

        else:

            principal = (principal - payout) * (1 + interest) 

            return balance(principal, interest, payout, duration-1)

    

    def deferred_annuity(interest):

        new_principal = deposit(principal, interest, gap)

        balance_amt = balance(new_principal, interest, payout, duration)

        return balance_amt

    return deferred_annuity

# e.g.

# test_balance = new_balance(1000, 2, 100, 2)

# result = test_balance(0.1)

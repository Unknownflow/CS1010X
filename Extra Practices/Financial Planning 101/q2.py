#Question 2

#Annuity

#An annuity is a series of payments made at fixed intervals of time. If you buy an annuity from a bank, you will pay a principal sum upfront, and then receive monthly or yearly payouts deducted from the principal. Your remaining principal will continue to earn compound interest in the meantime. Think of it as the opposite of a loan. Your task is to calculate how much you have left after receiving a certain number of payouts (or for the loan, how much you still owe after paying a certain number of installments).

#Define an function balance(principal, interest, payout, duration) that calculates the balance of an annuity right after receiving a certain number of payouts. interest is the monthly interest rate, payout is monthly and duration is just the number of payouts already received. Assume the first payout is made after 1 month.

#Hint: Consider the time interval in months instead of years. Your code should be similar to the previous one.



def balance(principal, interest, payout, duration):

    if duration == 0:

        return principal

    else:

        principal = principal * (1 + interest) - payout

        return balance(principal, interest, payout, duration-1)

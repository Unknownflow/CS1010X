#Question 1

#Compound interest

#Compound interest is interest added to the principal of a deposit or loan so that the added interest also earns interest from then on. For this training, we will assume that interest is compounded annually. This means that interest is earned each year and added back into the deposit. For example, at the start of year zero, we deposit $100 at 10% interest. At the start of year 1, we will have $100 x 1.1 = $110. In year 2, we have $110 x 1.1 = $121.
#Notice you have earned an additional $1 interest on the first $10 interest earned.

#Define an function deposit(principal, interest, duration) that outputs how much you will receive (including principal) at maturity for such a deposit. interest will be the effective annual rate of interest in decimal and duration will be in years.

#Definitions:

    #Principal refers to the initial amount you give.
    #Effective annual rate of interest here is just the annual interest rate (how much interest you earn in a year) since interest is compounded yearly. Being in decimal means a 10% interest is written as 0.1.
    #At maturity means at the end of the duration of deposit.


def deposit(principal, interest, duration):

    # formula : P (1 + r)**n

    result = principal * (1 + interest) ** duration

    return result

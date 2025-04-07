#Question 4

#CPF Life

#Now, you are ready to calculate the effective annual interest rate of CPF Life. The following, which is modelled as a deferred annuity, is a simplified case of the actual CPF Life scheme.

#The current minimum sum you have to contribute to CPF Life is $166,000 at 55 years old. This is your principal sum. At 65 years old, at the end of the first month, you will receive your first monthly payout of $1,280. The monthly payouts will last for 20 years for a total of 240 payouts. At the end of 20 years, there will be nothing left. Your task is to calculate the effective annual interest rate of this annuity.

#Define a function find_cpf_rate() which will calculate the effective annual interest rate of CPF Life. Note that the function takes in no inputs. Round off the output to 4 d.p. You may assume that new_balance has been defined for you.

#Hint: Use new_balance to generate a function that takes in an interest rate and outputs the balance left in the CPF Life after all payouts have been made. Now find the interest rate such that the output is zero. Remember that this is the monthly interest rate. The effective annual interest rate can be calculated using the following formula,

    #r = (1+j)**12 - 1,

#where r = effective annual interest rate and j = monthly interest rate.

def find_cpf_rate():

    principal = 166000

    gap = 10 * 12 + 1

    payout = 1280 

    duration = 240

    balance = new_balance(principal, gap, payout, duration)

    interest = 0

    while interest < 1: 

        balance_amt = balance(interest)

        if balance_amt >= 0:

            return round((1 + interest) ** 12 - 1, 4)

        

        interest += 0.000001

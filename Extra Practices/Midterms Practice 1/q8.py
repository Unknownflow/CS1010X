def count_change(amount, kind_of_coins):
    changeArr = [1, 5, 10, 20, 50, 100]
    def helper(amount, kind_of_coins):
        if amount == 0:
            return 1
        if amount < 0: 
            return 0
        if kind_of_coins < 0:
            return 0
        else:
            change = changeArr[kind_of_coins]

            if change > amount:
                return helper(amount, kind_of_coins-1)
            else:
                return helper(amount, kind_of_coins-1) + helper(amount-change, kind_of_coins)

    return helper(amount, kind_of_coins-1)

print(count_change(5,2))
print(count_change(10, 5))
print(count_change(20, 5))
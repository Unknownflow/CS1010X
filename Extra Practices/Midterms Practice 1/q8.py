def count_change(amount, kind_of_coins):
    changeArr = [1, 5, 10, 20, 50, 100]
    def helper(amount, kind_of_coins):
        if amount == 0:
            return 1
        if amount < 0: 
            return 0
        if kind_of_coins < 0:
            return 1
        else:
            #print(kind_of_coins)\

            if kind_of_coins - 1 < -1:
                return count_change(amount, -1)
            change = changeArr[kind_of_coins]
            print(change)
            if change > amount:
                return count_change(amount, kind_of_coins-1)
            else:
                return count_change(amount, kind_of_coins-1) + count_change(amount-change, kind_of_coins)

    return helper(amount, kind_of_coins-1)


#print(count_change(1,5))

#print(count_change(5,5))
#print(count_change(10, 5))
#print(count_change(20, 5))


print(count_change(5,2))

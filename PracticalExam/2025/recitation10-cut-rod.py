
print("==== Recitation #10: Memoization Version ====")

def cut_rod(n, prices):
    seen = {}
    def cut_rod_helper(n, prices):
        if n in seen:
            return seen[n]

        if n <= 0:
            return 0
        else:
            max_price = 0
            for p in prices: # p is the key of the dictionary
                if p <= n:
                    max_price = max( max_price, prices[p] + cut_rod_helper(n-p, prices))
        seen[n] = max_price
        return max_price
    return cut_rod_helper(n, prices)


prices1 = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}

print(cut_rod(45, prices1))

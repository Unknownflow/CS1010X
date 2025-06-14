


print("======memoization======")


def cut_rod_mm(n, prices):
    seen = {}
    def cut_rod_xx(n, prices, baggage):
        if n in seen:
            return seen[n]
    
        if n <=0:
            return 0,()
        else:
            max_price = 0
            for p in prices: # this is to go through all the options of cutting (key, which is the length)
                if p <= n:
                    temp_price, temp_bag = cut_rod_xx(n-p, prices, ())
                    if max_price < (prices[p]+temp_price):
                        max_price = prices[p]+temp_price
                        baggage = (p,) + temp_bag
                    
            seen[n] = (max_price, baggage)
            return max_price, baggage
    return cut_rod_xx(n, prices, ())



##
print("limiting....")

def cut_rod_limit_10m(m, n, prices):

    temp_prices = dict(prices)
    if 10 in prices:                
        temp_prices.pop(10)

    # use 1, use 2, use ..until n
    max_price = 0
    if 10 in prices:
        for i in range(m+1):
            if n-i*10 < 0:  # this is needed to make sure no error
                break
            temp_max, temp_baggage = cut_rod_mm(n - i*10, temp_prices)
            if temp_max + prices[10]*i > max_price:
                max_price = temp_max + prices[10]*i
                baggage = temp_baggage + (10,)*i
    else:
        max_price, baggage = cut_rod_mm(n, temp_prices)
    return (max_price, baggage)   

#############################
print("limiting.10 and 6...")
#seen = {}
def cut_rod_limit_10m_6k(m, k, n, prices):

    temp_prices = dict(prices)

    if 10 in prices:                
        temp_prices.pop(10)
        temp_10_price = prices[10]
    else:
        temp_10_price = 0
        
    if 6 in prices:
        temp_prices.pop(6)
        temp_6_price = prices[6]
    else:
        temp_6_price = 0

    # use 1, use 2, use ..until n
    max_price = 0
    for kk in range(k+1): # limit on 6
        for i in range(m+1):
            if n-(i*10 + kk*6) < 0:  # this is needed to make sure no error
                break
            temp_max, temp_baggage = cut_rod_mm(n - i*10 - kk*6, temp_prices)
            if temp_max + temp_10_price*i + temp_6_price*kk > max_price:
                max_price = temp_max + temp_10_price*i + temp_6_price*kk
                baggage = temp_baggage + (6,)*kk + (10,)*i 
                
    return (max_price, baggage)   


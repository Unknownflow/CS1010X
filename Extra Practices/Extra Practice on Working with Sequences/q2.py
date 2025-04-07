def tuplify(number):
    remainder = number % 10
    number = number // 10
    if number == 0:
        return (remainder,)
    else:
        return tuplify(number) + (remainder,)

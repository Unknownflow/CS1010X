class Number(object):
    # complete the class definition #
    def __init__(self, num):
        self.num = num
    
    def plus(self, number):
        if number.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num + number.num)

    def minus(self, number):
        if number.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num - number.num)
    
    def times(self, number):
        if number.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num * number.num)
    
    def divide(self, number):
        if self.value() == "Undefined" or number.value() == 0 or number.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(int(self.num / number.value()))

    def value(self):
        return self.num

### Uncomment the lines below ###

seventeen = Number(17)
four = Number(4)
zero = Number(0)

thirteen = seventeen.minus(four)
fiftytwo = thirteen.times(four)

blackjack=seventeen.plus(four)
something=blackjack.divide(zero)
another_thing=blackjack.plus(something)
something_else=another_thing.divide(blackjack)

### Uncomment the lines above ###

print(something.value())
print(another_thing.value())
print(something_else.value())
print(seventeen.value())
print(fiftytwo.value())
print(blackjack.value())
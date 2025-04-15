class Number(object):
    # complete the class definition #
    def __init__(self, num):
        self.num = num
    
    def plus(self, number):
        return Number(self.num + number.num)

    def minus(self, number):
        return Number(self.num - number.num)
    
    def times(self, number):
        return Number(self.num * number.num)
    
    def divide(self, number):
        return Number(int(self.num / number.num))

    def value(self):
        return self.num
        
### Uncomment the lines below ###
three=Number(3)
ten=Number(10)
seven=ten.minus(three)
twentyone=seven.times(three)
five=Number(5)
two=ten.divide(five)
### Uncomment the lines above ###

print(three.value())
print(ten.value())
print(seven.value())
print(twentyone.value())
print(five.value())
print(two.value())
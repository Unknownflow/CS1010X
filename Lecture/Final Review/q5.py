class Number(object):
    # complete the class definition #
    def __init__(self, num):
        self.num = num
        self.numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
                        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
                        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
                        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
                        20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 
                        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
        self.powers = {6: "million", 5: "hundred", 3: "thousand", 2: "hundred"}
    
    def times(self, number):
        if number.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num * number.num)
    
    def value(self):
        return self.num
    
    def spell(self):
        temp = str(self.num)
        power = len(temp) - 1
        if self.num > 10000000:
            return "really large number"
        else:
            string = ""
            num_idx = 0
            while num_idx < len(temp):
                num = int(temp[num_idx])

                if power == 0:
                    string += f"{self.numbers[num]}"
                elif power == 1:
                    if num == 0:
                        continue
                    elif num == 1:
                        num = int(temp[num_idx:num_idx+2])
                        string += f"{self.numbers[num]} "
                        power -= 1
                        num_idx += 1
                    else:
                        num *= 10
                        string += f"{self.numbers[num]} "
                elif power == 4:
                    if num == 0:
                        continue
                    elif num == 1:
                        num = int(temp[num_idx:num_idx+2])
                        string += f" and {self.numbers[num]} thousand, "
                        power -= 1
                        num_idx += 1
                    else:
                        num *= 10
                        string += f" and {self.numbers[num]} thousand, "
                elif power in self.powers:
                    if num != 0:
                        string += f"{self.numbers[num]} {self.powers[power]}"
                        if power == 3:
                            string += ", "
                        elif power == 2:
                            string += " and "
                        
                power -= 1
                num_idx += 1
            
            return string
    
### Uncomment the lines below ###
    
elite_number=Number(1337)
good_day_number=Number(210792)
bigno=good_day_number.times(elite_number)

### Uncomment the lines above ###

print(elite_number.spell())
print(good_day_number.spell())
print(bigno.spell())
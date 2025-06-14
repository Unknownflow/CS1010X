############## TOPIC 1 ###############
#
# Question 1
def make_mtf():
    mtf = []
    total_movement = 0
    def helper(fn, *args):
        nonlocal total_movement
        if fn == "is_empty":
            return len(mtf) == 0
        elif fn == "clear":
            mtf.clear()
        elif fn == "append":
            mtf.append(args[0])
        elif fn == "find":
            item = args[0]
            found = False
            end = len(mtf)
            curr = 0
            while curr < end and not found:
                if mtf[curr] == item:
                    found = True
                else:
                    curr += 1

            if not found:
                return -1

            total_movement += curr
            for i in range(curr, 0, -1):
                mtf[i], mtf[i-1] = mtf[i-1], mtf[i]

            return curr
        elif fn == "remove":
            item = args[0]
            if item in mtf:
                mtf.remove(item)
        elif fn == "list":
            return mtf
        elif fn == "movement":
            return total_movement
            
            
    return helper

m = make_mtf()
m("append",3)
m("append", 5)
m("append", 55)
m("append", 66)
print(m("list"))          # Ans: [3, 5, 55, 66]
print(m("find", 55))      # Ans: 2
print(m("list"))          # Ans: [55, 3, 5, 66]
print(m("movement"))      # Ans: 2
print(m("find", 66))      # Ans: 3
print(m("list"))          # Ans: [66, 55, 3, 5]
print(m("find", 56))      # Ans: -1
m("remove", 5)            # 5 in m is removed
m("remove", 56)           # No change to m
print(m("list"))          # Ans: [66, 55, 3]
print(m("movement"))      # Ans: 5


############## TOPIC 2 ###############
#   
# Question 2
#
from runes import *
def center_pic( pic1, pic2):
    return beside(stack(pic1, pic2), stack(pic2, pic1))

def side(pic, n):
    res = pic
    for i in range(n):
        res = stack_frac(i/(i+1), res, pic)
    return res
    

##show(side(heart_bb, 3))

#################
# Question 3
#
def top(pic, n):
    res = pic
    for i in range(n):
        res = stack_frac(i/(i+1), res, quarter_turn_left(pic))

    return quarter_turn_right(res)

##show(top(heart_bb, 3))

##############
# Question 4
#
def egyptian_with_corners ( ribbon_pic, center_pic, n):
    side_edge = side(ribbon_pic, n-2)
    side_edge = stack_frac(1/(n-1), center_pic, side_edge)
    side_edge = stack_frac((n-1)/n, side_edge, center_pic)

    top_edge = top(ribbon_pic, n-2)
    center = stack_frac(1/(n-1), top_edge, center_pic)
    center = stack_frac((n-1)/n, center, top_edge)

    top_and_center = stack_frac(1/(n-1), quarter_turn_left(side_edge), quarter_turn_left(center))
    top_and_center = stack_frac((n-1)/n, top_and_center, quarter_turn_left(side_edge))
    return quarter_turn_right(top_and_center) 

#show(egyptian_with_corners( heart_bb, center_pic(make_cross(nova_bb), make_cross(heart_bb)), 3))

show(egyptian_with_corners( heart_bb, center_pic(make_cross(nova_bb), make_cross(heart_bb)), 10))
     
############## TOPIC 3 ###############
#   
# Question 5
#

def cut_rod_mm(n, prices):
    max_price = [0] * (n+1)
    cuts = [[] for i in range(n+1)]
  
    for length in range(1, n+1):
        for p in prices:
            if p <= length:
                if max_price[length] < prices[p] + max_price[length-p]:
                    max_price[length] = prices[p] + max_price[length-p]
                    cuts[length] = cuts[length-p] + [p]
  
    return max_price[n], cuts[n]

##print(cut_rod_mm(45, {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}))
##print(cut_rod_mm(58, {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24}))

############## 
#   
# Question 6
#
def cut_rod_limit_10m (m, n, prices):
# parameter m is the limit on length 10, where n is the input rod length
    max_price = [0] * (n+1)
    cuts = [[] for i in range(n+1)]
  
    for length in range(1, n+1):
        for p in prices:
            if p <= length:
                if max_price[length] < prices[p] + max_price[length-p]:
                    if p == 10:
                        total_10 = cuts[length-p].count(10) + 1
                        if total_10 <= m:
                            max_price[length] = prices[p] + max_price[length-p]
                            cuts[length] = cuts[length-p] + [p]
                    else:
                        max_price[length] = prices[p] + max_price[length-p]
                        cuts[length] = cuts[length-p] + [p]
  
    return max_price[n], cuts[n]

#print(cut_rod_limit_10m(3, 45, {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}))
#print(cut_rod_limit_10m(2, 58, {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}))

############## 
#   
# Question 7
#
def cut_rod_limit_10m_6k(m, k, n, prices):
# Be careful: parameter m is for length 10, and k is for length 6. DO NOT MIX UP.
    max_price = [0] * (n+1)
    cuts = [[] for i in range(n+1)]
  
    for length in range(1, n+1):
        for p in prices:
            if p <= length:
                if max_price[length] < prices[p] + max_price[length-p]:
                    if p == 10:
                        total_10 = cuts[length-p].count(10) + 1
                        if total_10 <= m:
                            max_price[length] = prices[p] + max_price[length-p]
                            cuts[length] = cuts[length-p] + [p]
                    elif p == 6:
                        total_6 = cuts[length-p].count(6) + 1
                        if total_6 <= k:
                            max_price[length] = prices[p] + max_price[length-p]
                            cuts[length] = cuts[length-p] + [p]
                    else:
                        max_price[length] = prices[p] + max_price[length-p]
                        cuts[length] = cuts[length-p] + [p]
  
    return max_price[n], cuts[n]

#print(cut_rod_limit_10m_6k(2, 2, 45, {1:1, 2:5, 3:6, 4:9, 5:10, 6:17, 7:17, 8:20, 9:25, 10:30}))
#print(cut_rod_limit_10m_6k(2, 2, 58, {1:1, 2:5, 3:6, 4:9, 5:10, 6:17, 7:17, 8:20, 9:25, 10:30}))



############## TOPIC 4 ###############
#   
# Question 8
#
from math import floor, ceil
class nearest_neighbor(object):
    def __init__(self):
        self.neighbor_data = {}
        self.input_values = set()
	
    def data(self):
        return (len(self.input_values), self.input_values, self.neighbor_data)
	
    def add_data(self, new_data):
        upper_bound = ceil(new_data)
        lower_bound = floor(new_data)
        self.input_values.add(new_data)
        
        if upper_bound == lower_bound:
            if upper_bound in self.neighbor_data:
                if new_data not in self.neighbor_data[upper_bound]:
                    self.neighbor_data[upper_bound].append(new_data)
            else:
                self.neighbor_data[upper_bound] = [new_data]
        else:
            if upper_bound in self.neighbor_data:
                if new_data not in self.neighbor_data[upper_bound]:
                    self.neighbor_data[upper_bound].append(new_data)
            else:
                self.neighbor_data[upper_bound] = [new_data]

            if lower_bound in self.neighbor_data:
                if new_data not in self.neighbor_data[lower_bound]:
                    self.neighbor_data[lower_bound].append(new_data)
            else:
                self.neighbor_data[lower_bound] = [new_data]

    def find_nearest_neighbor(self, point):
        upper_bound = ceil(point)
        lower_bound = floor(point)
        min_diff = 10**8 + 1
        nearest_neighbor = []
        upper_neighbors = self.neighbor_data.get(upper_bound, [])
        lower_neighbors = self.neighbor_data.get(lower_bound, [])
        
        for neighbor in upper_neighbors:
            diff = abs(point * 10 ** 8 - neighbor * 10 ** 8)
            
            if diff > 10 ** 8:
                continue
            if diff == min_diff and neighbor not in nearest_neighbor:
                nearest_neighbor.append(neighbor)
            elif diff < min_diff:
                min_diff = diff
                nearest_neighbor = [neighbor]

        for neighbor in lower_neighbors:
            diff = abs(neighbor * 10 ** 8 - point * 10 ** 8)

            if diff > 10 ** 8:
                continue
            if diff == min_diff and neighbor not in nearest_neighbor:
                nearest_neighbor.append(neighbor)
            elif diff < min_diff:
                min_diff = diff
                nearest_neighbor = [neighbor]

        if not nearest_neighbor:
            return None
        return nearest_neighbor                
            

ps = nearest_neighbor()
ps.add_data(3.4) # first point added
ps.add_data(3.7) # second point added
ps.add_data(6.6) # third point added
ps.add_data(5.0) # fourth point added
ps.add_data(6.6) # duplicated point, so not added
print(ps.data())
#
# Ans: (4, {3.7,3.4,5.0,6.6}, {3: [3.4,3.7], 4: [3.4,3.7], 6: [6.6], 7: [6.6], 5:[5.0]})

print(ps.find_nearest_neighbor(7))          # Ans: [6.6]
print(ps.find_nearest_neighbor(7.7))        # Ans: None
print(ps.find_nearest_neighbor(3.54999999)) # Ans: [3.4]
print(ps.find_nearest_neighbor(3.55000001)) # Ans: [3.7]
print(ps.find_nearest_neighbor(3.55))       # Ans: [3.4,3.7]
##







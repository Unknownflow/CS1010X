# find point of at most 1 distance away -- in "constant" time
# no sorting,
# no library

from math import *   # not needed in coursemology.org submission
# use of floor, ceil

epsilon = 0.000000001 # if wrong setting of epsilon, can cause correct answer to be wrong

class nearest_neighbor(object):
    def __init__(self):
        self.no_of_data = 0
        self.dic = {}
        self.original_data = set({})

    def data(self):
        return (self.no_of_data,) + ( self.original_data,) + \
               (self.dic,)

    # all new_data are >= 0
    def add_data(self, new_data):
        def insert_data(at):
            if self.dic.get(at) == None:
                self.dic[at] = [new_data]
            else:
                self.dic[at].append(new_data)

        if new_data in self.original_data:
            return
        else:
            self.original_data.add(new_data)
            
        new_data_floor = floor(new_data)
        new_data_ceil  = ceil(new_data)
        if new_data_floor == new_data_ceil:
            # insert just 1
            insert_data(new_data_floor)   
                
        else: # insert 2
            insert_data(new_data_floor)   
            insert_data(new_data_ceil)
        self.no_of_data += 1
        

    def find_nearest_neighbor(self, point):
        def nearest_point(lst, point):
            if lst==[] or lst==None:  
                return None
            else:
                nearest = [ lst[0] ]
                distance = abs(lst[0] - point)
                for e in lst[1:]:
                    if (distance - abs(e - point)) > epsilon:
                        distance = abs(e - point)
                        nearest = [ e ]
                    elif (abs (abs(e - point) - distance)) < epsilon and e not in nearest:
                        nearest.append(e)
            return nearest

        lst = []
        if floor(point)==ceil(point): 
            lst = self.dic.get(point)
        else:  
            lst = []
            if self.dic.get(floor(point)) != None:
                lst = self.dic.get(floor(point))
            if self.dic.get(ceil(point)) != None:  
                lst = lst + self.dic.get(ceil(point))
    
        nearest = nearest_point(lst, point)

        if nearest!=None:
            if abs(nearest[0]-point)>1:
                nearest=None
        return nearest


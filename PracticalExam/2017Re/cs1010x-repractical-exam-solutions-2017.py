################
# Question 1A #
###############

def factors(n):
    ans = [1]
    for i in range(2,n):
        if n%i == 0:
            ans.append(i)
    ans.append(n)
    return ans

def test1a():
    print('=== Q1a ===')
    print(factors(2)==[1,2])
    print(factors(13)==[1,13])
    print(factors(18)==[1, 2, 3, 6, 9, 18])

def test1a_e():
    print('===Q1a(eval)===')
    print(factors(67)==[1, 67])
    print(factors(21)==[1, 3, 7, 21])
    print(factors(91)==[1, 7, 13, 91])
    print(factors(64)==[1, 2, 4, 8, 16, 32, 64])

#test1a()
#test1a_e()

###############
# Question 1B #
###############

def repetitions(s):
    factor_list = factors(len(s))
    factor_list.sort(reverse=True)
    for i in factor_list:
        length = len(s)//i
        success = True
        for j in range(1,i):
            if s[:length] != s[j*length:(j+1)*length]:
                success = False
                break
        if success:
            return i
    return 0

# Alternative solution - Murugesan Karthik
def repetitions(s):
    count = [1]
    for i in range(1, len(s)):
        x = s[:i]
        if x*(len(s)//len(x)) == s:
            count.append(len(s)/len(x))
    return int(max(count))

def test1b():
    print('=== Q1b ===')
    print(repetitions("aaaaa")==5)
    print(repetitions("ababab")==3)
    print(repetitions("abababc")==1)
    print(repetitions("abadbabcabadbabc")==2)

def test1b_e():
    print('=== Q1b(eval) ===')
    print(repetitions("")==1)
    print(repetitions("a")==1)
    print(repetitions("abcbabcba")==1)
    print(repetitions("bcabcabcabcad")==1)
    print(repetitions("abbabbabba")==1)
    print(repetitions("abbabbabbabb")==4)

#test1b()
#test1b_e()

##############
# Question 2 #
##############

import csv
def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)[1:]


###############
# Question 2A #
###############

def clean_data(filename):
    data = read_csv(filename)
    data = list(filter(lambda x: x[0]!="" and x[1]!="" and x[2]!="" and x[3]!="", data))
    data = list(filter(lambda x: x[4]!="" and 0<=float(x[4])<= 10, data))
    return list(filter(lambda x: x[5]!="" and 1916<= int(x[5])<=2016, data))
    
def test2a():
    print('=== Q2a ===')
    answer1 = [['Christopher Nolan', 'Adventure|Drama|Sci-Fi', 'Matthew McConaughey', 'Interstellar', '8.6', '2014'],\
          ['Alan Taylor', 'Action|Adventure|Sci-Fi', 'J.K. Simmons', 'Terminator Genisys', '8.6', '2015'],\
          ['Francis Lawrence', 'Adventure|Sci-Fi', 'Jennifer Lawrence', 'The Hunger Games: Mockingjay - Part 2', '8.6', '2015'], \
          ['Duncan Jones', 'Action|Adventure|Fantasy', 'Dominic Cooper', 'Warcraft', '8.6', '2016'], \
          ['James Bobin', 'Adventure|Family|Fantasy', 'Johnny Depp', 'Alice Through the Looking Glass', '8.6', '2016']]
    print(clean_data("IMDB_small.csv")==answer1)
    answer2 = [['A. Raven Cruz', 'Action|Adventure|Comedy|Fantasy|Sci-Fi', 'Scott Levy', 'The Helix... Loaded', '4.9', '2005'], \
               ['Aaron Hann', 'Drama|Horror|Mystery|Sci-Fi|Thriller', 'Jordi Vilasuso', 'Circle', '5.3', '2015']]
    print(clean_data("IMDB.csv")[:2]==answer2)

def test2a_e():
	print("=== Q2a(eval) ===")
	answer3 = [['Zal Batmanglij', 'Drama|Thriller', 'Alexander Skarsg\xc3\xa5rd', 'The East', '6', '2013'], \
				['Zoran Lisinac', 'Comedy|Music|Romance', 'Matthew Emerick', 'Along the Roadside', '3.9', '2013']]
	print(len(clean_data("IMDB.csv"))==4796)
	print(clean_data("IMDB.csv")[-2:]==answer3)

#test2a()
#test2a_e()

###############
# Question 2B #
###############

def best_movies(filename, genre, k):
    data = clean_data(filename)
    data = list(filter(lambda x: genre in x[1], data))
    data = list(map(lambda x: (x[3],x[4]), data))
    data.sort(key=lambda x: x[0])
    data.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], data))[:k]

def test2b():
    print('=== Q2b ===')
    print(best_movies("IMDB_small.csv", "Comedy",5)==[])
    print(best_movies("IMDB_small.csv", "Action",3)==['Terminator Genisys', 'Warcraft'])
    print(best_movies("IMDB.csv", "Comedy",5)==['Up', 'Monsters vs. Aliens', 'Evan Almighty', 'Suicide Squad', 'Wild Wild West'])
    print(best_movies("IMDB.csv", "Action",3)==['Jupiter Ascending', 'The Legend of Tarzan', 'The Dark Knight'])

def test2b_e():
	print('=== Q2c ===')
	print(best_movies("IMDB_small.csv", "Documentary", 2) == [])
	print(best_movies("IMDB_small.csv", "Adventure", 2) == ['Alice Through the Looking Glass', 'Interstellar'])
	print(best_movies("IMDB.csv", "Drama", 2) == ['The Legend of Tarzan', 'The Dark Knight'])
	print(best_movies("IMDB.csv", "Animation", 0)==[])

#test2b()
#test2b_e()

###############
# Question 2C #
###############

def best_actor(filename, start_year, end_year):
    
    count = {}
    data = clean_data(filename)
    for record in data:
        actor = record[2]
        rating = float(record[4])
        year = int(record[5])

        if start_year<=year<=end_year:
            if actor not in count:
                count[actor] = [0,0]
            count[actor][0] += 1
            count[actor][1] += rating
    
    for actor in count:
        count[actor] = count[actor][1]/count[actor][0]
    if not count:
        return None
    
    highest = max(count.values())
    ans = list(map(lambda x: x[0],list(filter(lambda x: x[1] == highest, list(count.items())))))
    if len(ans) == 1:
        return ans[0]
    else:
        return ans
    
def test2c():
    print('=== Q2c ===')
    print(best_actor("IMDB_small.csv", 1916, 1940)==None)
    print(sorted(best_actor("IMDB_small.csv", 1940, 2016)) == \
          sorted(['Matthew McConaughey', 'J.K. Simmons', 'Jennifer Lawrence', 'Dominic Cooper', 'Johnny Depp']))  
    print(best_actor("IMDB.csv", 1916, 1940)=="Mel Blanc")
    print(best_actor("IMDB.csv", 1941, 1990)=="Ronny Cox")
    print(best_actor("IMDB.csv", 1991, 2016)=="Steve Bastoni")

def test2c_e():
	print('=== Q2c(eval) ===')
	print(best_actor("IMDB_small.csv", 2000, 2006) == None)
	print(sorted(best_actor("IMDB.csv", 2000, 2000)) == sorted(['Tom Cruise', 'Karen Allen']))
	print(best_actor("IMDB.csv", 1990,1980) == None)
	print(best_actor("IMDB.csv", 1980,2001) == 'Jennifer Garner')
    
#test2c()
#test2c_e()

##############
# Question 3 #
##############

class SwimmingCompetition:

    def __init__(self,*args): # (laps, lanes)
        self.length = 50
        self.lanes = 8
        self.swimmers = {}
        self.laps = 2
        if len(args) > 0:
            self.laps = args[0] 
        if len(args) > 1:
            self.lanes = args[1]
        
    def add_swimmer(self, name, speed, turning):
        if len(self.swimmers) == self.lanes:
            return "No more lanes!"
        self.swimmers[name] = [speed,turning]

    def set_length(self,length):
        self.length = length

    def get_position(self, swimmer, t):
        if swimmer not in self.swimmers:
            return "No such swimmer"
        speed, turning = self.swimmers[swimmer]
        laps = 0
        lap_time = self.length/speed
        if t >= self.finish_time(swimmer): ## finished swimming
            return 0 if self.laps % 2 == 0 else self.length
        while t>lap_time:
            laps += 1
            t -= lap_time
            if t >= self.finish_time(swimmer):
                return 0 if self.laps % 2 == 0 else self.length
            if t < turning: # Stopped at turning
                if laps%2==0:
                    return 0
                else:
                    return self.length
            t -= turning
        if laps >= self.laps: # Finished swimming
            return 0
        elif laps%2==0:
            return t*speed
        else:
            return self.length-t*speed
        
    def finish_time(self, swimmer):
        if swimmer not in self.swimmers:
            return "No such swimmer"
        speed, turning = self.swimmers[swimmer]
        lap_time = self.length/speed
        return self.laps*lap_time + (self.laps-1)*turning

    def winner(self,*args):
        swimmers = list(self.swimmers.keys())
        times = list(map(lambda x: (x, self.finish_time(x)),swimmers))
        times.sort(key=lambda x:x[1])
        if not args:
            return times[0][0]
        else:
            winners = list(map(lambda x: x[0],times))
            return winners[:args[0]]

##################
# Marking scheme #
##################
# 1 mark  - multiple argument constructor taken care of correctly.
# 1 mark  - add_swimmer() takes care max lanes correctly
# 2 marks - finish time implemented correctly
# => 1 mark - one swimmer computed correctly
# => 1 mark - multiple swimmers correct. 
# 3 marks - winner implemented correctly
# => 2 marks - one winner computed correctly
# => 1 mark  - multiple winners correct. 
# 3 marks - get_position implemented correctly
# -1 mark if set_length is not implemented correctly.
# -1 mark if "No such swimmer" is not implemented correctly

def test3():
    def approx(v1,v2):
        return abs(v1-v2)<0.01
    
    print('=== Q3 ===')
    s1 = SwimmingCompetition()
    s1.add_swimmer("Joseph Schooling", 1.96, 0.39)
    s1.add_swimmer("Laszlo Cseh",1.955, 0.37)
    s1.add_swimmer("Tom Shields",1.953, 0.38)
    s1.add_swimmer("Michael Phelps",1.95, 0.42)
    s1.add_swimmer("Mehdy Metella",1.945, 0.42)
    print(approx(s1.finish_time("Joseph Schooling"),51.41))
    print(approx(s1.finish_time("Laszlo Cseh"),51.52))
    print(approx(s1.finish_time("Tom Shields"),51.58))
    print(approx(s1.finish_time("Michael Phelps"),51.70))
    print(approx(s1.finish_time("Mehdy Metella"),51.83))
    print(s1.winner()=="Joseph Schooling")
    print(s1.winner(2)==['Joseph Schooling', 'Laszlo Cseh'])
    print(s1.winner(5)==['Joseph Schooling', 'Laszlo Cseh', 'Tom Shields', 'Michael Phelps', 'Mehdy Metella'])
    print(s1.winner(6)==['Joseph Schooling', 'Laszlo Cseh', 'Tom Shields', 'Michael Phelps', 'Mehdy Metella'])
    print(approx(s1.get_position("Joseph Schooling",0),0.0))
    print(approx(s1.get_position("Joseph Schooling",10),19.6))
    print(approx(s1.get_position("Joseph Schooling",25.5),49.98))
    print(approx(s1.get_position("Joseph Schooling",25.7),50))
    print(approx(s1.get_position("Joseph Schooling",25.8),50))
    print(approx(s1.get_position("Joseph Schooling",26),49.80))
    print(approx(s1.get_position("Joseph Schooling",27),47.84))
    print(approx(s1.get_position("Joseph Schooling",50),2.76))
    print(approx(s1.get_position("Joseph Schooling",60),0))


    s2 = SwimmingCompetition(1,3)
    s2.add_swimmer("Joseph Schooling", 1.96, 0.39)
    s2.add_swimmer("Laszlo Cseh",1.955, 0.37)
    s2.add_swimmer("Tom Shields",1.953, 0.38)
    print(s2.add_swimmer("Michael Phelps",1.95, 0.42)=="No more lanes!")
    print(s2.add_swimmer("Mehdy Metella",1.945, 0.42)=="No more lanes!")
    print(s2.winner()=="Joseph Schooling")
    print(s2.winner(2)==['Joseph Schooling', 'Laszlo Cseh'])
    print(s2.winner(4)==['Joseph Schooling', 'Laszlo Cseh', 'Tom Shields'])
    print(s2.get_position("Trump",0)=="No such swimmer")

def test3_e():
	def approx(v1, v2):
		return abs(v1 - v2) < 0.01

	s3 = SwimmingCompetition(1, 1)
	s3.add_swimmer("Ben", 1.85, 0.5)
	print(s3.add_swimmer("Steven", 1.82, 0.2)=='No more lanes!')
	print(s3.winner()=='Ben')
	print(s3.winner(3)==['Ben'])
	print(approx(s3.finish_time('Ben'),27.03))

	s4 = SwimmingCompetition()
	s4.add_swimmer("Tom", 1.5, 0.45)
	s4.add_swimmer("Dick", 1.9, 0.9)
	s4.add_swimmer("Harry", 1.6, 0.7)
	print(s4.winner()=='Dick')
	print(s4.winner(2)==['Dick', 'Harry'])
	print(approx(s4.finish_time('Tom'), 67.12))
	print(approx(s4.get_position('Tom', 10), 15))
	print(approx(s4.get_position('Dick', 10), 19))
	print(approx(s4.get_position('Harry', 10), 16))

	s5 = SwimmingCompetition()
	s5.set_length(100)
	s5.add_swimmer('Trump', 0.5, 1)
	print(approx(s5.finish_time('Trump'), 401))
	print(approx(s5.get_position('Trump', 100), 50))

#test3()
#test3_e()

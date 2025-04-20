#################
# Q1a - Shuffle #
#################

def shuffle(a, times):
    if times == 0:
        return a
    else:
        shuffled = []
        length = len(a)
        mid = length // 2
        if length % 2 == 0:
            for i in range(mid):
                shuffled.append(a[i])
                shuffled.append(a[i+mid])
        else:
            for i in range(mid):
                shuffled.append(a[i])
                shuffled.append(a[i+mid+1])
            shuffled.append(a[mid])                
        a = shuffled
        return shuffle(a, times-1)

def test1a():
    print('=== Q1a ===')
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 1)==[1, 5, 2, 6, 3, 7, 4, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 2)==[1, 3, 5, 7, 2, 4, 6, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 3)==[1, 2, 3, 4, 5, 6, 7, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 1)==[1, 5, 2, 6, 3, 7, 4])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 2)==[1, 3, 5, 7, 2, 4, 6])
 
def test1a_e():
    print('=== Q1_e ===')
    '''
    Single shuffles - No recursion happens
    '''
    #Empty lists
    print(shuffle([], 1) == [])
    #Single element lists
    print(shuffle([3], 1) == [3])
    # Simple shuffle check. For even and odd number of elements
    print(shuffle([10, 11, 12, 13 , 14, 15, 16, 17], 1) == [10, 14, 11, 15, 12, 16, 13, 17])
    print(shuffle([10, 11, 12, 13, 15, 16, 17], 1) == [10, 15, 11, 16, 12, 17, 13])
    # Check against the assumption that the list in sorted
    print(shuffle([9, 8, 7, 6, 5, 4, 3], 1) == [9, 5, 8, 4, 7, 3, 6])
    #print(shuffle([7, 2, 6, 1, 3, 49, 22, 21], 1) == [7, 3, 2, 49, 6, 22, 1, 21])    
    # Check for being type agnostic
    #print(shuffle([ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 1) == ['A', 8, 2, 9, 3, 10, 4, 'J', 5, 'Q', 6, 'K', 7])
    '''
    Multiple shuffles - Check for recursion
    '''
    #Empty lists
    print(shuffle([], 7) == [])
    #Single element lists
    print(shuffle([9], 2) == [9])
    # Simple shuffle check. For even and odd number of elements
    print(shuffle([1, 2, 3], 2) == [1, 2, 3])
    #print(shuffle([10, 11, 12, 13 , 14, 15, 16, 17], 17) == [10, 12, 14, 16, 11, 13, 15, 17])
    #print(shuffle([10, 11, 12, 13, 15, 16, 17], 3) == [10, 11, 12, 13, 15, 16, 17])
    # Check against the assumption that the list in sorted
    #print(shuffle([9, 8, 7, 6, 5, 4, 3], 11) == [9, 7, 5, 3, 8, 6, 4])
    print(shuffle([7, 2, 6, 1, 3, 49, 22, 21], 7) == [7, 3, 2, 49, 6, 22, 1, 21])    
    # Check for being type agnostic
    print(shuffle([ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 2) == ['A', 'J', 8, 5, 2, 'Q', 9, 6, 3, 'K', 10, 7, 4])
    '''
    shuffling list of lists!
    '''
    print(shuffle([[1, 2, "buckle my show"],[3, 4, "lock the door"],[5, 6, "pick up the sticks"],[7, 8, "lay them straight"],23,"asgard",22.3], 1) == [[1, 2, 'buckle my show'], 23, [3, 4, 'lock the door'], 'asgard', [5, 6, 'pick up the sticks'], 22.3, [7, 8, 'lay them straight']])

# test1a()
# test1a_e()


##########################
# Q1b - Back to Original #
##########################

def back_to_original(a):
    count = 0
    orig = a
    while True:
        a = shuffle(a, 1)
        count += 1
        if a == orig:
            return count
        

def test1b():
    print('=== Q1b ===')    
    print(back_to_original([1, 2, 3, 4, 5, 6, 7, 8])==3)
    print(back_to_original([1, 2, 3, 4, 5])==4)
    print(back_to_original([1, 1, 1, 1])==1)
 
def test1b_e():
    print('=== Q1b_e ===')
    #empty lists
    print(back_to_original([])==1)

    #single element lists
    print(back_to_original([3])==1)

    #Single shuffle returns
    print(back_to_original([0, 0, 0, 0])==1)
    print(back_to_original([1, 2, 2, 1])==1)

    # arbitrary shuffles
    print(back_to_original([1, 1, 1, 2, 2, 2])==4)
    print(back_to_original([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])==10)
    #print(back_to_original([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])==10)

    print(back_to_original([0, 0, 0, 1, 0])==4)
    print(back_to_original([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])==4)
    print(back_to_original([1, 2, 1, 1])==2)

    #type agnostic shuffles
    print(back_to_original([[1, 2, "buckle my show"],[3, 4, "lock the door"],[5, 6, "pick up the sticks"],[7, 8, "lay them straight"],23,"asgard",22.3])==3)

# test1b()
# test1b_e()


##############
# Question 2 #
##############

import csv
from datetime import datetime

def read_csv(csvfilename):
	"""
	Reads a csv file and returns a list of list
	containing rows in the csv file and its entries.
	"""
	rows = []

	with open(csvfilename) as csvfile:
		file_reader = csv.reader(csvfile)
		for row in file_reader:
			rows.append(row)
	return rows

###############
# Question 2a #
###############

def get_dates_for_hashtag(filename, hashtag):
    rows = read_csv(filename)
    dates = []
    for row in rows:
        date, time, tweet, hashtags, likes, retweets = row
        hashtags_list = hashtags.split(";")
        if hashtag in hashtags_list:
            if date not in dates:
                dates.append(date)
    
    return dates

def test2a():
    print("===2a===")
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ObamacareFail")	
    tweets.sort()
    print(tweets == ['16-10-25', '16-10-29', '16-10-31'])
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ElectionDay")
    tweets.sort()
    print(tweets == ['16-08-09', '16-11-08'])
    print(get_dates_for_hashtag("donald-tweets.csv", "China")==[]) 

def test2a_e():
    print("===2a_e===")
    tweets = get_dates_for_hashtag("donald-tweets.csv", "vaticanwalls")	
    print(tweets == ['16-02-19'])
    tweets = get_dates_for_hashtag("donald-tweets.csv", "IranDeal")
    print(set(tweets) == set(['15-09-09', '15-08-28', '15-08-11', '15-07-28']))
    #print(set(get_dates_for_hashtag("donald-tweets.csv", "India"))==set(['16-04-27']))
    #print(set(get_dates_for_hashtag("donald-tweets.csv", "BigLeagueTruth"))==set(['16-10-20', '16-10-10', '16-10-05', '16-10-03']))
    print(set(get_dates_for_hashtag("donald-tweets.csv", "RIGGED"))==set(['16-10-18']))
    print(set(get_dates_for_hashtag("donald-tweets.csv", "RiggedSystem"))==set(['16-10-17', '16-07-05'])) 

    # print(get_dates_for_hashtag('modi-tweets-cleaned.csv', 'gqworld')==['11-09-21'])

# test2a()
# test2a_e()

###############
# Question 2b #
###############

def active_hour(filename,start_date,end_date):
    start_date = datetime.strptime(start_date + " 00:00:00", "%y-%m-%d %X")
    end_date = datetime.strptime(end_date + " 23:59:59", "%y-%m-%d %X")
    rows = read_csv(filename)
    hours_count = {}
    for row in rows[1:]:
        date, time, tweet, hashtags, likes, retweets = row
        date = datetime.strptime(date + " " + time, "%y-%m-%d %X")
        if start_date <= date <= end_date:
            hour = date.hour
            if hour not in hours_count:
                hours_count[hour] = 1
            else:
                hours_count[hour] += 1
    
    max_count = 0
    max_hour = []
    for hour, count in hours_count.items():
        if count == max_count:
            max_hour.append(hour)
        elif count > max_count:
            max_hour = [hour]
            max_count = count
    print(max_hour)
    return sorted(max_hour)
    
def test2b():
    print("===2b===")
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-08")==[21])
    print(active_hour("donald-tweets.csv", "16-08-23", "16-11-06")==[1])
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-06")==[0, 23])

# test2b()


###############
# Question 2c #
###############

def top_k(filename,k,start_date,end_date):
    start_date = datetime.strptime(start_date + " 00:00:00", "%y-%m-%d %X")
    end_date = datetime.strptime(end_date + " 23:59:59", "%y-%m-%d %X")
    rows = read_csv(filename)
    tweets = []
    for row in rows[1:]:
        date, time, tweet, hashtags, likes, retweets = row
        likes = int(likes)
        date = datetime.strptime(date + " " + time, "%y-%m-%d %X")

        if start_date <= date <= end_date:
            tweets.append((tweet, likes))
    sorted_tweets = sorted(tweets, key=lambda x: x[1], reverse=True)
    top_tweets = []

    for i in range(min(k, len(sorted_tweets))):
        top_tweets.append(sorted_tweets[i][0])
    
    return top_tweets
    
def test2c():
    print("===2c===")
    tweets = ['TODAY WE MAKE AMERICA GREAT AGAIN!']
    print(top_k("donald-tweets.csv", 1, "16-11-08", "16-11-08")==tweets)
    tweets = ['The media is spending more time doing a forensic analysis of Melanias speech than the FBI spent on Hillarys emails.', 'Such a great honor to be the Republican Nominee for President of the United States. I will work hard and never let you down! AMERICA FIRST!', 'Here is my statement. https://t.co/WAZiGoQqMQ']
    print(top_k("donald-tweets.csv", 3, "15-10-13", "16-10-11")==tweets)
    print(top_k("donald-tweets.csv", 1, "16-11-18", "16-11-20")==[])

def test2c_e():
    print("===2c_e===")
    tweets = ['TODAY WE MAKE AMERICA GREAT AGAIN!']
    print(top_k("donald-tweets.csv", 1, "16-11-08", "16-11-08")==tweets)
    tweets = ['The media is spending more time doing a forensic analysis of Melanias speech than the FBI spent on Hillarys emails.', 'Such a great honor to be the Republican Nominee for President of the United States. I will work hard and never let you down! AMERICA FIRST!', 'Here is my statement. https://t.co/WAZiGoQqMQ']
    print(top_k("donald-tweets.csv", 3, "15-10-13", "16-10-11")==tweets)
    print(top_k("donald-tweets.csv", 1, "16-11-18", "16-11-20")==[])
    tweets = top_k("donald-tweets.csv", 2, "15-07-18", "15-07-18")
    ans = ['Its a national embarrassment that an illegal immigrant can walk across the border and receive free health care and one of our Veterans.....', '....that has served our country is put on a waiting list and gets no care.']
    print(tweets == ans)

# test2c()
# test2c_e()


##############
# Question 3 #
##############
 
class Student:
    course_namelist = {}

    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_courses(self, *courses):
        for course in courses:
            self.courses.append(course)
            if course not in Student.course_namelist:
                Student.course_namelist[course] = [self]
            else:
                Student.course_namelist[course].append(self)

    def drop_courses(self, *courses):
        for course in courses:
            if course in self.courses:
                self.courses.remove(course)
                Student.course_namelist[course].remove(self)

    def get_courses(self):
        return self.courses
            
    def common_courses(self,other):
        common_course = []
        for course in self.courses:
            for other_course in other.courses:
                if course == other_course:
                    common_course.append(course)
        
        return common_course

    def is_coursemate(self,other):
        if self.common_courses(other) == []:
            return False
        else:
            return True

    def common_friends(self,other):
        my_friends = self.get_friends()
        other_friends = other.get_friends()
        common_friend = []

        for friend in my_friends:
            if friend in other_friends and friend not in common_friend:
                if friend.name not in common_friend:
                    common_friend.append(friend.name)
        
        return common_friend

    def six_degrees(self,other):
        other_name = other.get_name()
        def helper(friends):
            if len(friends) == 0:
                return 0
            if len(friends) == 1:
                if friends[0].name == other_name:
                    return 1
                else:
                    return 0
            else:
                first = helper([friends[0]])
                rest = helper(friends[1:])
                print(first, rest)
                if first == 0 or rest == 0:
                    return 0
                else:
                    return min(first, rest)
        
        friends = self.get_friends()
        res = helper(friends)
        print(res)
        if res == 0:
            return None
        else:
            return res
    
    def get_friends(self):
        courses = self.get_courses()
        friends = []

        for course in courses:
            namelist = Student.course_namelist[course]
            for student in namelist:
                if student.name not in friends:
                    friends.append(student)
        
        return friends

    def get_name(self):
        return self.name

# sample execution
def test3():
    print("===3===")
    benj = Student("Ben Junior")
    benj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS2016", "GEM2455")
    tanj = Student("Tan Junior")
    tanj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS3243")
    amanda = Student("Amanda See")
    amanda.add_courses("GEM1010", "CS1014",  "CS1231", "CS2017", "GEM2455")
    ad = Student("Ad Lee")
    ad.add_courses("CS1010", "CS1000", "CS2010", "CS2040", "CS1207")
    ayush = Student("Ayush")
    ayush.add_courses("MA1016", "MA1014", "MA2050", "MA2016")

    print(benj.is_coursemate(tanj))
    print(benj.is_coursemate(amanda))
    print(benj.is_coursemate(ad))
    print(benj.is_coursemate(ayush)==False)
    print(benj.common_courses(tanj)==['CS1010', 'CS1014', 'CS2010', 'CS2060'])
    print(benj.common_courses(amanda)==['CS1014', 'GEM2455']) # Found interesting girl in class!
    print(benj.common_courses(ad)==['CS1010', 'CS2010'])
    print(benj.common_courses(ayush)==[])

    amanda.drop_courses("CS1014", "GEM2455") # She disappears from our class :'(
    amanda.add_courses("CS3243")
    print(benj.is_coursemate(amanda)==False)
    print(benj.common_courses(amanda)==[]) # Girl disappears
    print(amanda.get_courses()==['GEM1010', 'CS1231', 'CS2017', 'CS3243']) # What is she taking now? 

    print(benj.six_degrees(amanda)==2) # How can we get to know her?
    print(benj.common_friends(amanda)==['Tan Junior'])
    print(amanda.common_courses(tanj)==['CS3243'])

    tanj.drop_courses("CS3243")
    print(benj.six_degrees(amanda)==None) 
    print(benj.common_friends(amanda)==[])

    amanda.add_courses("MA2050")
    ayush.add_courses("CS1000")
    print(benj.six_degrees(amanda)==3)

    
# test3()

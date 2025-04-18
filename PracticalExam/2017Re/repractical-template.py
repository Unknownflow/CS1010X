###############
# Question 1A #
###############

def factors(n):
    # Your answer here
    pass

def test1a():
    print('=== Q1a ===')
    print(factors(2)==[1,2])
    print(factors(13)==[1,13])
    print(factors(18)==[1, 2, 3, 6, 9, 18])
#test1a()

###############
# Question 1B #
###############

def repetitions(s):
    # Your answer here
    pass

def test1b():
    print('=== Q1b ===')
    print(repetitions("aaaaa")==5)
    print(repetitions("ababab")==3)
    print(repetitions("abababc")==1)
    print(repetitions("abadbabcabadbabc")==2)
#test1b()

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
    # Your answer here
    pass
    
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
#test2a()

###############
# Question 2B #
###############

def best_movies(filename, genre, k):
    # Your answer here
    pass


def test2b():
    print('=== Q2b ===')
    print(best_movies("IMDB_small.csv", "Comedy",5)==[])
    print(best_movies("IMDB_small.csv", "Action",3)==['Terminator Genisys', 'Warcraft'])
    print(best_movies("IMDB.csv", "Comedy",5)==['Up', 'Monsters vs. Aliens', 'Evan Almighty', 'Suicide Squad', 'Wild Wild West'])
    print(best_movies("IMDB.csv", "Action",3)==['Jupiter Ascending', 'The Legend of Tarzan', 'The Dark Knight'])
#test2b()
    
###############
# Question 2C #
###############

def best_actor(filename, start_year, end_year):
    # Your answer here
    pass
    
def test2c():
    print('=== Q2c ===')
    print(best_actor("IMDB_small.csv", 1916, 1940)==None)
    print(sorted(best_actor("IMDB_small.csv", 1940, 2016)) == \
          sorted(['Matthew McConaughey', 'J.K. Simmons', 'Jennifer Lawrence', 'Dominic Cooper', 'Johnny Depp']))
    print(best_actor("IMDB.csv", 1916, 1940)=="Mel Blanc")
    print(best_actor("IMDB.csv", 1941, 1990)=="Ronny Cox")
    print(best_actor("IMDB.csv", 1991, 2016)=="Steve Bastoni")

#test2c()

##############
# Question 3 #
##############

class SwimmingCompetition:
    # Your answer here
    pass

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
    print(s2.get_position("Trump",0)=="No such swimmer"))

#test3()
            


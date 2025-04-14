import csv
from math import sqrt

##############
# Question 1 #
##############


###################
# Q1a - In circle #
###################

def digit_product(n):
    product = 1
    while n != 0:
        remainder = n % 10
        product *= remainder
        n = n // 10
    return product

def test1a():
    print('=== Q1a ===')
    print(digit_product(1111)==1)
    print(digit_product(123)==6)
    print(digit_product(123041)==0)

# test1a()



########################
# Q1b - Furthest Apart #
########################

def max_digit_product(n,k):
    product = 1
    max_product = 0
    n = str(n)
    for i in range(len(n)-k+1):
        for j in range(i, i+k):
            product *= int(n[j])
            if product > max_product:
                max_product = product
        product = 1
    
    return max_product

def test1b():
    print('=== Q1b ===')
    print(max_digit_product(11123,1)==3)
    print(max_digit_product(11123,2)==6)
    print(max_digit_product(1111111,5)==1)
    print(max_digit_product(189113451,2)==72)

# test1b()


###########################
# Q2 - Show me the Money! #
###########################
# These functions are provided for you
# Do not make any changes to them

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)
def count_NA_employment(data):
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):
    return len(list(filter(lambda x: x[5] == "NA", data)))

#######
# Q2A #
#######

def parse_data(filename):
    lines = read_csv(filename)
    data = []
    idx = 1
    length = len(lines) - 1

    while idx < length:
        year, university, school, degree, variable, value = lines[idx]
        next_year, next_university, next_school, next_degree, next_variable, next_value = lines[idx+1]
        year = int(year)
        value = float(value)
        next_year = int(year)
        next_value = float(next_value)

        if (year == next_year and 
            university == next_university and 
            school == next_school and 
            degree == next_degree):
            idx += 2
            if variable == "employment_rate_overall":
                employment_rate_overall = value
            else:
                basic_monthly_median = value
            
            if next_variable == "employment_rate_overall":
                employment_rate_overall = next_value
            else:
                basic_monthly_median = next_value
        else:
            idx += 1
            if variable == "employment_rate_overall":
                employment_rate_overall = value
                basic_monthly_median = "NA"
            else:
                employment_rate_overall = "NA"
                basic_monthly_median = value
        
        data_item = [year, university, school, degree, employment_rate_overall, basic_monthly_median]
        data.append(data_item)
    return data

def count_NA_employment(data):   # Helper for testing
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):       # Helper for testing
    return len(list(filter(lambda x: x[5] == "NA", data)))

def test2a():
    print('=== Q2a ===')
    print(len(parse_data("employment.csv"))==179)
    print(count_NA_employment(parse_data("employment.csv"))==1)
    print(count_NA_salary(parse_data("employment.csv"))==1)

# test2a()

#######
# Q2B #
#######

def compute_employment_rate(filename,university,degree,start,end):
    data = parse_data(filename)
    total_rate = 0
    date_found = False
    year_count = 0
    for row in data:
        year, university_data, school, degree_data, employment_rate_overall, basic_monthly_median = row
        if start <= year <= end and \
            university == university_data and \
            degree == degree_data:
            if employment_rate_overall != "NA":
                date_found = True
                total_rate += employment_rate_overall
                year_count += 1
    
    if date_found:
        return total_rate / year_count
    else:
        return "NA"

def test2b():
    print('=== Q2b ===')
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)==100.0)
    print(compute_employment_rate("employment.csv",'Nanyang Technological University', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2014,2014)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Computing (Computer Science)",2014,2018)==93.8)

# test2b()

#######
# Q2C #
#######

def top_k_degree(filename,start,end,k):
    data = parse_data(filename)
    salary_dict = {}
    for row in data:
        year, university, school, degree, employment_rate_overall, basic_monthly_median = row
        if start <= year <= end:
            key = (degree, university)
            if basic_monthly_median != "NA":
                if key in salary_dict:
                    if salary_dict[key]["prev_median"] >= basic_monthly_median:
                        salary_dict[key] = {
                            "total_median": 0, 
                            "prev_median": 0,
                            "missing_data": True,
                            "year_count": 0
                            }                    
                    else:
                        total_median = salary_dict[key]["total_median"]
                        year_count = salary_dict[key]["year_count"]
                        salary_dict[key] = {
                            "total_median": total_median + basic_monthly_median,
                            "prev_median": basic_monthly_median,
                            "missing_data": False,
                            "year_count": year_count + 1
                            }

                else:
                    salary_dict[key] = {
                        "total_median": basic_monthly_median, 
                        "prev_median": basic_monthly_median,
                        "missing_data": False,
                        "year_count": 1
                        }
                    
            else:
                salary_dict[key] = {
                        "total_median": 0, 
                        "prev_median": 0,
                        "missing_data": True,
                        "year_count": 0
                        }
    non_missing = []
    for key, value in salary_dict.items():
        if not value["missing_data"] and value["year_count"] == (end-start+1):
            non_missing.append((key, value))

    if len(non_missing) == 0:
        return []
    
    non_missing = sorted(non_missing, key=lambda x: x[1]["total_median"], reverse=True)

    res = []
    total_count = 0
    for item in non_missing:
        if total_count < k:
            res.append(list(item[0]))
            total_count += 1
            prev = item[1]["total_median"]
        else:
            break
    
    for i in range(k, len(non_missing)):
        item = non_missing[i]
        # print('s', prev, non_missing[:5])
        if item[1]["total_median"] == prev:
            res.append(list(item[0]))
        else:
            break

    return res
    

def test2c():
    print('=== Q2c ===')
    print(top_k_degree("employment.csv",2014,2015,3)==\
          [['Business and Computing', 'Nanyang Technological University'],\
           ['Bachelor of Engineering (Computer Engineering)', 'National University of Singapore'], \
           ['Bachelor of Business Administration (Hons)', 'National University of Singapore']])
    print(top_k_degree("employment.csv",2014,2018,3)==[])

test2c()

################################
# Q3 - Social Network Security #
################################

privacy_settings = ["private", "friends", "FOF", "public"]
# private = no one can read
# friends = friends can read
# FOF = friends of friends can read
# public = anyone can read

class User:
    pass

def test3():
    print('=== Q3 ===')
    ben = User("Ben")
    oana = User("Oana")
    chenhao = User("Chenhao")
    clement = User("Clement")

    print(ben.is_friend(oana)==False)
    print(ben.is_friend(chenhao)==False)
    print(ben.accept(oana)==False)

    print(oana.request(ben)==True)
    print(oana.request(chenhao)==True)
    print(oana.request(chenhao)==False)
    print(oana.is_friend(ben)==False)
    print(oana.is_friend(chenhao)==False)

    print(ben.accept(oana)==True)
    print(chenhao.request(oana)==True)
    print(oana.is_friend(ben)==True)
    print(oana.is_friend(chenhao)==True)

    ben.post("CS1010X is fun")
    ben.post("No tutorials next week","FOF")
    ben.post("Did you remember to order pizza?","friends")
    ben.post("Exam grading will be done on Tuesday.")
    ben.post("Finals will be very difficult","private")

    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    ben.post("Finals will be very difficult")
    ben.update_privacy("Finals will be very difficult","public")
    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Finals will be very difficult'])
    print(clement.read_posts(ben) == ['CS1010X is fun', 'Finals will be very difficult'])

    ben.update_privacy("Finals will be very difficult","friends")
    print(ben.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(oana.read_posts(ben)== ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    ben.update_privacy("Finals will be very difficult","friends")
    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

    print(oana.unfriend(chenhao)==True)
    print(oana.unfriend(chenhao)==False)
    print(oana.is_friend(chenhao)==False)

    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

#test3()

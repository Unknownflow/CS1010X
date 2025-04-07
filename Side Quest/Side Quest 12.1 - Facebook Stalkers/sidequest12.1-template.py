#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json('cs1010x-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    # Returns the total number of comments
    feedData = data["feed"]["data"]
    comments_count = 0

    for feed in feedData:
        if "comments" in feed:
            commentsData = feed["comments"]["data"]
            comments_count += len(commentsData)

    return comments_count

# print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    # Returns the total number of likes (in feed posts and comments)
    feedData = data["feed"]["data"]
    likes_count = 0

    for feed in feedData:
        if "likes" in feed:
            likes_count += len(feed["likes"]["data"])

        if "comments" in feed:
            commentsData = feed["comments"]["data"]

            for comment in commentsData:
                likes_count += comment["like_count"]

    return likes_count

# print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    # Lookup table where key is id and value is member data object
    membersData = data["members"]["data"]
    lookupTable = {}

    for data in membersData:
        id = data["id"]
        dataObj = {}
        
        for key, val in data.items():
            if key != "id":
                dataObj[key] = val

        lookupTable[id] = dataObj
    
    return lookupTable


member_dict = create_member_dict(fb_data)
# print(member_dict["10205702832196255"])

# Q: Why did we choose the id of the member data object to be the key?
# A: The id is a unique identifier to identify the member and the key must be unique for each member as if there are 
# two members with the same identifier, it will result in a collision in the dict and more work is needed to resolve 
# this collision.

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: If there are two people with the identical names, they would have the same key and when trying to lookup the name
# in the lookup table, they will lookup at the same position in the lookup table and this results in a collision. More
# work will thus be needed to resolve this collsion.

##########
# Task d #
##########

def posts_freq(data):
    # Returns a dict where key is fb_id and value is number of posts in feed
    posts_freq_dict = {}
    feed_data = data["feed"]["data"]

    for feed in feed_data:
        id = feed["from"]["id"]

        if id not in posts_freq_dict:
            posts_freq_dict[id] = 1
        else:
            posts_freq_dict[id] += 1

    return posts_freq_dict

# print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    # Returns a dict where key is fb_id and value is number of comments in feed
    comments_freq_dict = {}
    feed_data = data["feed"]["data"]

    for feed in feed_data:
        if "comments" in feed:
            comments_data = feed["comments"]["data"]

            for comment in comments_data:
                id = comment["from"]["id"]

                if id not in comments_freq_dict:
                    comments_freq_dict[id] = 1
                else:
                    comments_freq_dict[id] += 1
    
    return comments_freq_dict

# print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    # Returns a dict where key is fb_id and value is number of likes in feed
    likes_freq_dict = {}
    feed_data = data["feed"]["data"]

    for feed in feed_data:
        if "likes" in feed:
            likes_data = feed["likes"]["data"]

            for like in likes_data:
                id = like["id"]
                if id not in likes_freq_dict:
                    likes_freq_dict[id] = 1
                else:
                    likes_freq_dict[id] += 1
        
    return likes_freq_dict

# print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    # Returns a dict where key is fb_id and value is the number of likes
    # a person's posts and comments have
    popularity_score_dict = {}
    feed_data = data["feed"]["data"]

    for feed in feed_data:
        if "likes" in feed:
            likes_data = feed["likes"]["data"]
            id = feed["from"]["id"]

            if id not in popularity_score_dict:
                popularity_score_dict[id] = len(likes_data)
            else:
                popularity_score_dict[id] += len(likes_data)
        
        if "comments" in feed:
            comments_data = feed["comments"]["data"]

            for comment in comments_data:
                id = comment["from"]["id"]
                like_count = comment["like_count"]

                if id not in popularity_score_dict:
                    if like_count != 0:
                        popularity_score_dict[id] = like_count
                else:
                    popularity_score_dict[id] += like_count

    return popularity_score_dict

# print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    # Expand the member dict to include the keys:
    # 'posts_count', 'comments_count' and 'likes_count'
    member_dict = create_member_dict(data)
    post_dict = posts_freq(data)
    comment_dict = comments_freq(data)
    like_dict = likes_freq(data)

    for key in member_dict.keys():
        if key not in post_dict:
            member_dict[key]["posts_count"] = 0
        else:
            member_dict[key]["posts_count"] = post_dict[key]
        
        if key not in comment_dict:
            member_dict[key]["comments_count"] = 0
        else:
            member_dict[key]["comments_count"] = comment_dict[key]
        
        if key not in like_dict:
            member_dict[key]["likes_count"] = 0
        else:
            member_dict[key]["likes_count"] = like_dict[key]
        
    return member_dict

stats = member_stats(fb_data)
# print(stats["10152805891837166"])

##########
# Task i #
##########

def activity_score(data):
    member_stat = member_stats(data)
    post_points = 3
    comment_points = 2
    like_points = 1
    activity_dict = {}

    for key in member_stat.keys():
        score = 0
        stats = member_stat[key]
        score += stats["posts_count"] * post_points
        score += stats["comments_count"] * comment_points
        score += stats["likes_count"] * like_points
        activity_dict[key] = score
    
    return activity_dict


scores = activity_score(fb_data)
# print(scores["10153020766393769"]) # => 30
# print(scores["857756387629369"]) # => 8


##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    # This is a higher order function, where type is a function and
    # can be either posts_freq, comments_freq, likes_freq, etc
    # and filters out the pairs that have frequency >= k
    member_dict = create_member_dict(data)
    active_members_arr = []
    freq_data = type_fn(data)
    freq_data = dict(filter(lambda val: val[1] >= k, freq_data.items()))

    for key, val in freq_data.items():
        if key in member_dict:
            name = member_dict[key]["name"]
            active_members_arr.append([name, val])
            
    active_members_arr.sort(key=lambda x: (-x[1], x[0]))
    return active_members_arr

# print(active_members_of_type(fb_data, 2, posts_freq))

# print(active_members_of_type(fb_data, 20, comments_freq))

# print(active_members_of_type(fb_data, 40, likes_freq))

# print(active_members_of_type(fb_data, 4, likes_freq))

# print(active_members_of_type(fb_data, 20, popularity_score))

# print(active_members_of_type(fb_data, 80, activity_score))




########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()

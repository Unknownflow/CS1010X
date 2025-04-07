from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *

def httpget(url):
    parsed = urlsplit(url)
    if not parsed.scheme:  # protocol insertion
        url = 'http://' + url
    elif parsed.scheme != 'http':
        raise ValueError("Unknown protocol")
    return urlopen(url).read()

url = "http://www.nus.edu.sg/"

# Q5
"""
Fill in your answer here.
The user may not be able to find the webpage as the webpage might have been
moved to another address, hence resulting in an error 404. The user may also 
not be authorised to access the website and this result in error 403. 
"""

#Q6
"""
Fill in your answer here.
If an empty string is returned, the user will not know what is happening when 
the URL is not accessible. When an error message is returned, it allows the user to 
know what is happening.
"""

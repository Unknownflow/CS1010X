from urllib.request import *
from urllib.parse import *
from urllib.error import *

URLS = [["","impossible.txt"],["http://google.com/cs1010fc","fail.txt"]]

class InternetFail(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) 
## Do not remove the lines above.

def httpget(url):
    parsed = urlsplit(url)
    if not parsed.scheme: #protocol insertion
        url = 'http://'+url
    elif parsed.scheme != 'http':
        raise ValueError("Unknown protocol")
    
    try:
        return urlopen(url).read()
    except HTTPError as err:
        raise InternetFail(err)
    except URLError as err:
        raise ValueError(err)
    except Exception as err:
        raise err

def download_URLs(URL_filenames):
    # Your code here
    for url_filename in URL_filenames:
        url, filename = url_filename
        try:
            contents = httpget(url)
            with open(filename, 'wb') as myFile: 
                myFile.write(contents)
        except Exception as err:
            raise err


download_URLs(URLS)
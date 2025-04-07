from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *

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
    except HTTPError:
        raise InternetFail("Internet fail")
    except URLError:
        raise ValueError("Url error")
    except Exception:
        raise "error"


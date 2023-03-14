import json,random
from os import path

def quote():
    _path = path.dirname(__file__)
    _path = path.join(_path,"quotes/quotes.json")
    _quotes = json.loads(open(_path, 'rb').read())
    _quote = _quotes[random.randint(0,len(_quotes)-1)]
    return (_quote['text'],_quote['from'])

# print(type(quote()))
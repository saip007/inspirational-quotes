import json,random
from os import path

def quote():
    dirpath = path.dirname(__file__)
    dirpath = path.join(dirpath,"quotes/quotes.json")
    quotes = json.loads(open(dirpath, 'rb').read())
    quote = quotes[random.randint(0,len(quotes)-1)]
    result = {'quote':quote['text'],"author":quote['from']}
    return result



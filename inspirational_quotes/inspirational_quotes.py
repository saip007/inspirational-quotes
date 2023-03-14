import json,random

def quote():
    _quotes = json.loads(open('inspirational_quotes/inspirational_quotes/quotes/quotes.json', 'rb').read())
    _quote = _quotes[random.randint(0,len(_quotes)-1)]
    return (_quote['text'],_quote['from'])

# print(type(quote()))
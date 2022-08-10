from urllib.request import urlopen
import urllib
import json

def get_ticker(q):
    url = ("https://financialmodelingprep.com/api/v3/search")
    ctx = {"query":str(q),
    "apikey":"90bb3a3ee4fd0b262dd3e63381ec5739"}
    # post_args = urllib.urlencode(ctx)
    query_string = urllib.parse.urlencode( ctx ) 
    url = url + "?" + query_string 
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

print(get_ticker("Google"))
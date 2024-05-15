from json import load
from pprint import pprint
from urllib.request import Request, urlopen


req = Request('https://ok.surf/api/v1/news-section')
req.add_header('accept', 'application/json')
req.add_header('Content-Type', 'application/json')
response = load(urlopen(req))
pprint(response)
  


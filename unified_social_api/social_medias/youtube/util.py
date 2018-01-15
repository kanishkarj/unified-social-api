from urllib.parse import urlencode
from urllib import request
import json


def call_gdata(api, qs):
    qs = dict(qs)
    qs['key'] = "AIzaSyDvysm00R5FClmqtxcATsgpKHdt2GxCaiU"
    url = 'https://www.googleapis.com/youtube/v3/' + api + '?' + urlencode(qs)

    data = request.urlopen(url).read().decode('utf-8')

    return json.loads(data)

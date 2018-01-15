from urllib.parse import urlencode
from urllib import request
import json
import re
from ...abstract.feed import Feed
from ...abstract.story import Story


class channel(Feed):
    def _getStories(self, keyword):
        uploads = get_channel_uploads(keyword)
        youtube_videos = []
        for item in uploads['items']:
            d = dict(url='https://www.youtube.com/watch?v='+item['snippet']['resourceId']['videoId'],
                     title=item['snippet']['title'],
                     pub_time=item['snippet']['publishedAt'].replace(".000Z", "").replace("T", " "),
                     content=item['snippet']['description'],
                     source='youtube',
                     thumb='http://i.ytimg.com/vi/'+item['snippet']['resourceId']['videoId']+'/mqdefault.jpg')
            youtube_videos.append(Story('youtube.'+keyword, d))

        return youtube_videos


def call_gdata(api, qs):
    qs = dict(qs)
    qs['key'] = "AIzaSyDvysm00R5FClmqtxcATsgpKHdt2GxCaiU"
    url = 'https://www.googleapis.com/youtube/v3/' + api + '?' + urlencode(qs)

    data = request.urlopen(url).read().decode('utf-8')

    return json.loads(data)


def get_channel_uploads(url):
    query = None
    chanR = re.compile('.+channel\/([^\/]+)$')
    userR = re.compile('.+user\/([^\/]+)$')
    channel_id = None
    channel_url = url
    if chanR.match(channel_url):
        channel_id = chanR.search(channel_url).group(1)
    elif userR.match(channel_url):
        username = userR.search(channel_url).group(1)
        query = {'part': 'snippet, contentDetails, statistics',
                 'forUsername': username}
    elif len(channel_url) == 24 and channel_url[:2] == 'UC':
        channel_id = channel_url
    else:
        username = channel_url
        query = {'part': 'snippet, contentDetails, statistics',
                 'forUsername': username}

    if query is None:
        query = {'part': 'snippet, contentDetails, statistics',
                 'id': channel_id}
    allinfo = call_gdata('channels', query)

    try:
        ch = allinfo['items'][0]
    except IndexError:
        err = "Unrecognized channel id, url or name : %s"
        raise ValueError(err % channel_url)

    return get_uploads(ch['contentDetails']['relatedPlaylists']['uploads'])


def get_uploads(upload_id):
    query = {'part': 'snippet',
             'maxResults': 50,
             'playlistId': upload_id}

    data = call_gdata('playlistItems', query)

    return data

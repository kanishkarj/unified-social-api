# unified-social-api
An Unified API for various soicial media platforms

## Development Insructions

### Make a new social media

Make a new directory under social_medias for adding a new social media. The property of the social media should be a new python file of the same name and it should contain a class of the same name. 

The class should inherit from Feed class in abstract.
The social media class should define the fucntion ```_getStories(keyword)``` and this function should return a list of ```Story``` items.

The ```Story``` item take 2 arguments for initialisation; 
- ```identity``` - Source of ```Story``` item. Ex: ```youtube.channel.thenewboston```
- ```d``` - A dictionary of items containing, for example, title, url, etc.

Sample code:
```python
# social_medias/facebook/group.py

from ...abstract import Feed, Story

class group(Feed):
  def _getStories(keyword):
    items = getItems(keyword)
    
    return_data = []
    
    for item in items:
      d = dict(title=item.title
               url=item.url
               content=item.content)
               
      return_data.append(Story('facebook.group.'+keyword, d))
     
    return return_data
```

### Testing the new social media

From the root of the repository, launch python interpretor.
```python
>>> import unified_social_api as usa
>>> pclub = usa.get_object('facebook.group', 'pclubiiti')
>>> pclub
Sources: facebook
Length: 27
>>>
>>> tnb = usa.get_object('youtube.channel', 'thenewboston')
>>> tnb
Sources: youtube
Length: 50
>>>
>>> pclub.extend(tnb)
>>> pclub
Sources: facebook, youtube
Length: 77

```

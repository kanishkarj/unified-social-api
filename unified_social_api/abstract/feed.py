import json
from abc import ABCMeta, abstractmethod


class Feed(metaclass=ABCMeta):
    def __init__(self, keyword):
        self._stories = []
        self._len = len(self._stories)
        self.__iter__ = self._stories.__iter__
        self._stories = self._getStories(keyword)
        try:
            self.sources = [self._stories[0].source]
        except IndexError:
            # TODO: No results
            raise

        self._len = len(self._stories)

    @abstractmethod
    def _getStories(self, keyword):
        pass

    def __repr__(self):
        sources = ', '.join(source for source in self.sources)
        length = self._len

        rep = "Sources: {0}\nLength: {1}".format(sources, length)

        return rep

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        return self._stories[index]

    def __setitem__(self, index, value):
        self._stories[index] = value

    def append(self, story):
        self._stories.append(story)
        self._len += 1
        if story.source not in self.sources:
            self.sources.append(story.source)

    def extend(self, feed):
        self._stories.extend(feed)
        self._len += len(self._stories)
        for source in feed.sources:
            if source not in self.sources:
                self.sources.append(source)

    def sortByTime(self, reverse):
        self._stories.sort(key=lambda x: x.published, reverse=reverse)

    def sortByPopularity(self):
        pass

    def toJson(self):
        res = []
        for x in self._stories:
            res.append(x.__dict__)
        return json.dumps(res)

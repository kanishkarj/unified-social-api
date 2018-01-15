class Story:
    def __init__(self, identity, d):  # source and identity mandatory
        self.source = identity.split('.')[0]
        self.identity = identity
        self.__dict__.update(d)

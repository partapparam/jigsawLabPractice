class Artist:
    attributes = ['name', 'popularity', 'id']

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.attributes:
                setattr(self, k, v)
                
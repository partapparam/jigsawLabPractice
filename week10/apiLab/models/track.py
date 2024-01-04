class Track:
    attributes = ['id', 'name', 'album_name', 'duration_ms']

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.attributes:
                setattr(self, k, v)
    
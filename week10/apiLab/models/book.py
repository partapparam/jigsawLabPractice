class Book:
    attributes = ['id', 'title', 'author_name', 'published']

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.attributes:
                setattr(self, k, v)
    
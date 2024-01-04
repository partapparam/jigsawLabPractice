class Author:
    attributes = ['id', 'work_count', 'name']

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.attributes:
                setattr(self, k, v)
                
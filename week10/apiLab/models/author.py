class Author:
    attributes = ['id', 'birth_date', 'top_work', 'work_count', 'name']

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.attributes:
                setattr(self, k, v)
                
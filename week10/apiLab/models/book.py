class Book:
    attributes: list[str] = ['id', 'title', 'author_name', 'published']

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if k in self.attributes:
                setattr(self, k, v)
    
class Author:
    attributes: list[str] = ['id', 'work_count', 'name']

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if k in self.attributes:
                setattr(self, k, v)
                
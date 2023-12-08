class Actor:
    columns = ['id', 'name']

    def __init__(self, *data):
        self.__dict__ = dict(zip(self.columns, data))
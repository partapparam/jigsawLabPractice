class Movie:
    columns = ['id', 'title', 'studio', 'runtime', 'description', 'release_date', 'year']

    def __init__(self, *data):
        self.__dict__ = dict(zip(self.columns, data))
class Seat:
    __table__ = 'seats'
    columns = ['id', 'seats']

    def __init__(self, **kwargs): 
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
            
        for k, v in kwargs.items():
            setattr(self, k, v)
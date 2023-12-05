class Player:
    columns = ['id', 'name', 'age', 'height', 'weight', 
               'shot', 'birth_place', 'birthdate', 'number']
    # we are converting columns and values to a dict
    # then we are assiging it to __dict__ property of our model
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
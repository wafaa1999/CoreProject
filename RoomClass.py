class Room:
    def __init__(self, number, type):
        self._number = number
        self._type = type

    def get_number(self): return self._number

    def get_type(self): return self._type

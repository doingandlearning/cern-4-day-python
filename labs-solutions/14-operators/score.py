from datetime import date
from datetime import datetime

class Score:
    def __init__(self, value=0):
        self.value = value
        self.day = date.today()
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")

    # Define a set of methods to provide operator functionality

    def __add__(self, other):
        if isinstance(other, Score):
            new_value = self.value + other.value
            return Score(new_value)
        else:
            raise ValueError(f'Invalid type {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Score):
            new_value = self.value - other.value
            return Score(new_value)
        else:
            raise ValueError(f'Invalid type {type(other)}')

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __str__(self):
        return f'Score[{self.value} {self.day} {self.current_time} ]'

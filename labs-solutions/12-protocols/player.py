
class Player:
    """ Class to represent a player within the number guess game """

    def __init__(self, name):
        self.name = name
        self.guess_count = 0
        self.history = []

    def __repr__(self):
        return f'Player {self.name} - history {self.history}'

    def increment_count(self):
        self.guess_count = self.guess_count + 1

    def add_guess(self, guess):
        self.history.append(guess)

    def print_history(self):
        formatted_history = list(map(lambda guess: f'\t guess: {guess}', self.history))
        for guess in formatted_history:
            print(guess)

    # Implement the length Protocol
    def __len__(self):
        return len(self.history)

    # Makes this class Iterable
    def __iter__(self):
        return self.history.__iter__()


player1 = Player('John')
print(player1)

player1.increment_count()
player1.add_guess(4)

player1.increment_count()
player1.add_guess(2)

print(player1)
print(len(player1))

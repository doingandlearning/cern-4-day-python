class Player:
    """ Class to represent a player within the number guess game """

    def __init__(self, name, count=0, history=[]):
        self.name = name
        self.guess_count = count
        self.history = history

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player {self.name} - history {self.history} - guess_count {self.guess_count}'

    def increment_count(self):
        self.guess_count = self.guess_count + 1

    def add_guess(self, guess):
        self.history.append(guess)

    def print_history(self):
        for guess in self.history:
            print(f'\t guess: {guess}')


player1 = Player('John')
print(player1)

player1.increment_count()
player1.add_guess(4)
player1.increment_count()
player1.add_guess(2)
print(player1)

print('History:')
player1.print_history()

player2 = Player('Denise')
players = [player1, player2]
print(players)

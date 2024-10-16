class Player:
    """ Class to represent a player within the number guess game """

    def __init__(self, name: str, count:int =0, history=[]):
        self.name = name
        if type(count) != type(1):
            raise ValueError("Count needs to be a integer")
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


while True:
    previous_count = input("What was your previous count??")
    try:
        player1 = Player(True, count=int(previous_count))
        player1.add_guess(4)
        player1.add_guess(6)
        player1.print_history()
        print(player1.name)
        print(player1.guess_count)
    except:
        print("Opps that should have been a number!")
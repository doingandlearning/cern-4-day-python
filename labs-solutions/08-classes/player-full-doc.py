class Player:
    """
    Class to represent a player within the number guess game.

    Attributes
    ----------
    name : str
        The name of the player.
    guess_count : int
        The number of guesses made by the player.
    history : list
        A list to store the history of guesses made by the player.
    """

    def __init__(self, name, count=0, history=None):
        """
        Initialize a new Player instance.

        :param str name: The name of the player.
        :param int count: The number of guesses made by the player (default is 0).
        :param list history: A list of guesses made by the player (default is empty).
        """
        self.name = name
        self.guess_count = count
        self.history = history if history is not None else []

    def __repr__(self):
        """
        Return a formal string representation of the Player object.
        
        :return: A string representing the player.
        :rtype: str
        """
        return f'Player({self.name})'

    def __str__(self):
        """
        Return a readable string representation of the player's name, guess count, and guess history.
        
        :return: A string with the player's details.
        :rtype: str
        """
        return f'Player {self.name} - history {self.history} - guess_count {self.guess_count}'

    def increment_count(self):
        """
        Increment the player's guess count by 1.
        """
        self.guess_count += 1

    def add_guess(self, guess):
        """
        Add a new guess to the player's guess history.

        :param guess: The player's guess to be added.
        :type guess: int
        """
        self.history.append(guess)

    def print_history(self):
        """
        Print out the player's guess history in a formatted manner.
        """
        for guess in self.history:
            print(f'\t guess: {guess}')

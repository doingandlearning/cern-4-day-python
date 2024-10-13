# Illustrates creating a history with information
# on the result of each guess i.e. was it higher or lower

import random
from functools import reduce

# Set up some global 'constants'
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = 'Please guess a number between ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + ': '



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

    def make_a_guess(self):
        guess = get_user_guess(GUESS_PROMPT)
        if guess != -1:
            self.increment_count()
        return guess


def welcome_message():
    print('Welcome to the number guess game')


def get_user_yes_or_no(prompt):
    """ get input from the user and check that it is y or n"""
    invalid_input = True
    while invalid_input:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print('Input Error - Input must be "y" or "n"')


def display_instructions():
    response = get_user_yes_or_no('Do you want to see the instructions?: ')
    if response == 'y':
        print(GUESS_PROMPT)
        print("You can play as many times as you like")








def get_user_guess(prompt):
    user_input_int = None
    invalid_input = True
    while invalid_input:
        user_input = input(prompt)
        if user_input == '-1':
            return -1
        if not user_input.isdigit():
            print('Input must be a positive number')
        else:
            user_input_int = int(user_input)
            if user_input_int < MIN_VALUE or user_input_int > MAX_VALUE:
                print(f'Number must be in range {MIN_VALUE} and {MAX_VALUE}')
            else:
                invalid_input = False
    return user_input_int




class Game:

    def __init__(self):
        # Low score dictionary
        self.low_score_dictionary = {}
        # current player
        self.current_player = None

    def play_game(self):
        # Set up main game loop variable
        game_over = False
        while not game_over:

            # Initialise the number to be guessed
            number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

            # display instructions if required
            display_instructions()
            # Check the current user setting
            self.check_current_user()

            # Initialise the players history of guesses
            self.current_player.history = []

            # Obtain their initialise guess
            guess = 0
            while number_to_guess != guess and self.current_player.guess_count != MAX_NUMBER_OF_GUESSES:

                # Set up a message to user variable
                message_to_user = ''

                guess = self.current_player.make_a_guess()

                # Check to see they have not exceeded the maximum
                # number of attempts if so break out of loop otherwise
                # give the user come feedback
                if guess == -1:
                    print('The number to guess is', number_to_guess)
                    continue
                elif number_to_guess == guess:
                    message_to_user = 'Correct Guess'
                elif self.current_player.guess_count == MAX_NUMBER_OF_GUESSES:
                    message_to_user = 'Max number of guesses made'
                elif guess + 1 == number_to_guess or guess - 1 == number_to_guess:
                    message_to_user = 'Sorry wrong number - you were out by 1'
                elif guess < number_to_guess:
                    message_to_user = "Sorry wrong number\nYour guess was lower than the number"
                elif guess > number_to_guess:
                    message_to_user = 'Sorry wrong number\nYour guess was higher than the number'

                print(message_to_user)

                # Add the guess to the history and increment number of attempts
                self.current_player.add_guess((guess, message_to_user))

            # Check to see if they did guess the correct number
            if number_to_guess == guess:
                print('Well done you won!')
                print(f'You took {self.current_player.guess_count} goes to complete the game')
            else:
                print("Sorry - you loose")
                print(f'The number you needed to guess was {number_to_guess}')

            self.update_low_score_table(self.current_player.name, self.current_player.guess_count)

            # Present the guess history
            print('Your guesses were:')
            self.current_player.print_history()

            play_again = input("Do you want to play again? ")
            if play_again.lower() == 'n' or play_again.lower() == 'no':
                game_over = True

    def check_current_user(self):
        check_new_user = 'n'
        if self.current_player is not None:
            user_prompt = f'The current user is {self.current_player.name}, do you wish to enter a new name (y/n): '
            check_new_user = input(user_prompt).lower()

        if check_new_user == 'y' or self.current_player is None:
            name = input('Please input your name: ')
            self.current_player = Player(name)

    def game_over_message(self):
        print('Game Over')
        print('Low Score table:')
        for key in self.low_score_dictionary:
            print(f'\t{key.name} = {self.low_score_dictionary[key]}')

        print('-' * 25)
        self.analyse_low_score_table()

    def update_low_score_table(self, user, count_number_of_tries):
        previous_low_score = self.low_score_dictionary.get(user, 1000)
        if previous_low_score > count_number_of_tries:
            self.low_score_dictionary[self.current_player] = count_number_of_tries

    def analyse_low_score_table(self):
        low_score_length = len(self.low_score_dictionary)
        print(f'Number of scores in low score table: {low_score_length}')
        func = lambda total, item: total + item[1]
        low_score_total = reduce(func, self.low_score_dictionary.items(), 0)
        low_score_average = low_score_total / low_score_length
        print(f'Average of low scores: {low_score_average}')
        # Filter scores
        scores_above_three = list(filter(lambda item: item[1] > 2, self.low_score_dictionary.items()))
        print(f'Scores above 3 {scores_above_three}')
        scores_in_ascending_order = sorted(self.low_score_dictionary.items(), key=lambda item: item[1])
        print(f'Scores in ascending order {scores_in_ascending_order}')
        scores_in_descending_order = sorted(self.low_score_dictionary.items(),
                                            reverse=True,
                                            key=lambda item: item[1])
        print(f'Scores in descending order {scores_in_descending_order}')
        # chain HOF for filter and sorting
        scores_in_ascending_order_above_three = sorted(filter(lambda item: item[1] > 2, self.low_score_dictionary.items()),
                                                       key=lambda item: item[1])
        print(f'Scores in ascending order above three {scores_in_ascending_order_above_three}')
        scores_in_descending_order_above_three = sorted(filter(lambda item: item[1] > 2, self.low_score_dictionary.items()),
                                                        reverse=True,
                                                        key=lambda item: item[1])
        print(f'Scores in descending order above three {scores_in_descending_order_above_three}')


welcome_message()
game = Game()
game.play_game()
game.game_over_message()

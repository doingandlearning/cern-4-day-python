# Illustrates creating a history with information
# on the result of each guess i.e. was it higher or lower

import random
import traceback

# Set up some global 'constants'
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = f'Please guess a number between {MIN_VALUE} and {MAX_VALUE}: '

# Set up global variables
# Low score dictionary
low_score_dictionary = {}
# current player
current_player = None


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


def game_over_message():
    print('Game Over')
    print('Low Score table:')
    for key in low_score_dictionary:
        print(f'\t{key} = {low_score_dictionary[key]}')

    print('-' * 25)
    analyse_low_score_table()


def check_current_player():
    global current_player
    check_new_user = 'n'
    if current_player is not None:
        user_prompt = f'The current user is {current_player}, do you wish to enter a new name (y/n): '
        check_new_user = input(user_prompt).lower()

    if check_new_user == 'y' or current_player is None:
        current_player = input('Please input your name: ')

    if current_player == '':
        raise ValueError('Invalid Name')


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


def generate_number_to_guess(start=MIN_VALUE, end=MAX_VALUE):
    number_to_guess = random.randint(start, end)
    return number_to_guess


def update_low_score_table(user, count_number_of_tries):
    previous_low_score = low_score_dictionary.get(user, 1000)
    if previous_low_score > count_number_of_tries:
        low_score_dictionary[current_player] = count_number_of_tries


def analyse_low_score_table():
    low_score_length = len(low_score_dictionary)
    print(f'Number of scores in low score table: {low_score_length}')

    # Filter scores
    scores_above_three = list(filter(lambda item: item[1] > 2, low_score_dictionary.items()))
    print(f'Scores above 3 {scores_above_three}')
    scores_in_ascending_order = sorted(low_score_dictionary.items(), key=lambda item: item[1])
    print(f'Scores in ascending order {scores_in_ascending_order}')
    scores_in_descending_order = sorted(low_score_dictionary.items(),
                                        reverse=True,
                                        key=lambda item: item[1])
    print(f'Scores in descending order {scores_in_descending_order}')
    # chain HOF for filter and sorting
    scores_in_ascending_order_above_three = sorted(filter(lambda item: item[1] > 2, low_score_dictionary.items()),
                                                   key=lambda item: item[1])
    print(f'Scores in ascending order above three {scores_in_ascending_order_above_three}')
    scores_in_descending_order_above_three = sorted(filter(lambda item: item[1] > 2, low_score_dictionary.items()),
                                                    reverse=True,
                                                    key=lambda item: item[1])
    print(f'Scores in descending order above three {scores_in_descending_order_above_three}')


def play_game():
    # Set up main game loop variable
    game_over = False
    while not game_over:

        # Initialise the history of guesses
        history = []

        # Initialise the number to be guessed
        number_to_guess = generate_number_to_guess()

        # Initialise the number of tries the player has made
        count_number_of_tries = 0

        # display instructions if required
        display_instructions()
        # Check the current user setting
        check_current_player()

        # Obtain their initialise guess
        guess = 0
        while number_to_guess != guess and count_number_of_tries != MAX_NUMBER_OF_GUESSES:

            # Set up a message to user variable
            message_to_user = ''

            guess = get_user_guess(GUESS_PROMPT)

            # Check to see they have not exceeded the maximum
            # number of attempts if so break out of loop otherwise
            # give the user come feedback
            if guess == -1:
                print('The number to guess is', number_to_guess)
                continue
            elif number_to_guess == guess:
                message_to_user = 'Correct Guess'
            elif count_number_of_tries + 1 == MAX_NUMBER_OF_GUESSES:
                message_to_user = 'Max number of guesses made'
            elif guess + 1 == number_to_guess or guess - 1 == number_to_guess:
                message_to_user = 'Sorry wrong number - you were out by 1'
            elif guess < number_to_guess:
                message_to_user = "Sorry wrong number\nYour guess was lower than the number"
            elif guess > number_to_guess:
                message_to_user = 'Sorry wrong number\nYour guess was higher than the number'

            print(message_to_user)

            # Add the guess to the history and increment number of attempts
            history.append((guess, message_to_user))

            # Obtain their next guess and increment number of attempts
            count_number_of_tries += 1

        # Check to see if they did guess the correct number
        if number_to_guess == guess:
            print('Well done you won!')
            print(f'You took {count_number_of_tries} goes to complete the game')
        else:
            print("Sorry - you loose")
            print(f'The number you needed to guess was {number_to_guess}')

        update_low_score_table(current_player, count_number_of_tries)

        # Present the guess history
        print('Your guesses were:')
        print(history)

        def format_entry(entry):
            return f'{"-" * 25}\nGuess[{entry[0]}]\n{entry[1]}'

        print([format_entry(entry) for entry in history])

        play_again = input("Do you want to play again? ")
        if play_again.lower() == 'n' or play_again.lower() == 'no':
            game_over = True


try:
    welcome_message()
    play_game()
    game_over_message()
except ValueError as exp:
    print('Handling exception')
    print(exp)
    traceback.print_exc()

print('Done')

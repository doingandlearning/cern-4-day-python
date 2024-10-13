# Illustrates creating a history with information
# on the result of each guess i.e. was it higher or lower

import random

# Set up some global 'constants'
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = f'Please guess a number between {MIN_VALUE} and {MAX_VALUE}: '

# Current player
current_player = None

# Low score dictionary
low_score_dictionary = {}

# Set up variables to be used in the game
game_over = False
while not game_over:

    # Initialise the history of guesses
    history = []

    # Initialise the number to be guessed
    number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    # Start the game
    print('Welcome to the number guess game')

    check_new_user = 'n'
    if current_player is not None:
        user_prompt = f'The current user is {current_player}, do you wish to enter a new name (y/n): '
        check_new_user = input(user_prompt).lower()

    if check_new_user == 'y' or current_player is None:
        current_player = input('Please input your name: ')

    continue_to_guess = True
    while continue_to_guess:

        # Set up a message to user variable
        message_to_user = None

        # Obtain their initialise guess
        guess = int(input(GUESS_PROMPT))

        # Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if guess == -1:
            print('The number to guess is', number_to_guess)
            continue
        elif number_to_guess == guess:
            message_to_user = 'Correct Guess'
            continue_to_guess = False
        elif count_number_of_tries + 1 == MAX_NUMBER_OF_GUESSES:
            message_to_user = 'Max number of guesses made'
            continue_to_guess = False
        elif guess + 1 == number_to_guess or guess - 1 == number_to_guess:
            message_to_user = 'Sorry wrong number - you were out by 1'
        elif guess < number_to_guess:
            message_to_user = "Sorry wrong number\nYour guess was lower than the number"
        elif guess > number_to_guess:
            message_to_user = 'Sorry wrong number\nYour guess was higher than the number'

        print(message_to_user)

        # Add the guess to the history and increment number of attempts
        guess_record = (guess, message_to_user)
        history.append(guess_record)

        # Obtain their next guess and increment number of attempts
        count_number_of_tries += 1

    # Check to see if they did guess the correct number
    if number_to_guess == guess:
        print('Well done you won!')
        print(f'You took {count_number_of_tries} goes to complete the game')

        previous_low_score = low_score_dictionary.get(current_player, 1000)
        if previous_low_score > count_number_of_tries:
            low_score_dictionary[current_player] = count_number_of_tries

    else:
        print("Sorry - you loose")
        print(f'The number you needed to guess was {number_to_guess}')

    # Present the guess history
    print('Your guesses were:')
    print(history)

    total = 0
    lowest_value = 9999
    highest_value = -1
    for item in history:
        total = total + item[0]
        if lowest_value > item[0]:
            lowest_value = item[0]
        if highest_value < item[0]:
            highest_value = item[0]

    print(f'The lowest value entered: {lowest_value}')
    print(f'The highest value entered: {highest_value}')
    print(f'Average value is: {total / len(history)}')

    input_not_accepted = True
    while input_not_accepted:
        play_again = input("Do you want to play again (y/n) or (yes/no)? ")
        play_again = play_again.lower()
        if play_again == 'n' or play_again == 'no':
            game_over = True
            input_not_accepted = False
        elif play_again == 'y' or play_again == 'yes':
            input_not_accepted = False
        else:
            print('Invalid input must be y/n or yes/no')

print('Game Over\n')

print('-' * 20)
print('Low Score table:')
print('-' * 20)
for key in low_score_dictionary:
    print(f'\t{key} = {low_score_dictionary[key]}')

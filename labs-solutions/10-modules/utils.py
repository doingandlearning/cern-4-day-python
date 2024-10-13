

def get_user_yes_or_no(prompt):
    """ get input from the user and check that it is y or n"""
    invalid_input = True
    while invalid_input:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print('Input Error - Input must be "y" or "n"')
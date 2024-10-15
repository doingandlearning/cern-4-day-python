count = 10
GUESS_PROMPT = "Some generic"

player_dictionary = {"illegal": [1,23,3], "offensive": [2,2,4]}


def data_check_player_names():
    global player_dictionary
    for value in ["illegal", "offensive"]:
        del player_dictionary[value]

data_check_player_names()
print(player_dictionary)

def some_func(count):
    # global GUESS_PROMPT
    # GUESS_PROMPT = "Something less generic"
    count = count + 1
    print(count)
    return "Something less generic"

GUESS_PROMPT = some_func(count)
print(count)


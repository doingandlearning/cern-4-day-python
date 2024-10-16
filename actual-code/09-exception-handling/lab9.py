while True:
    try:
        # How to handle if the string is empty?
        user_name = input("What is your username? ")
        if not user_name: ## or if user_name == "":
            raise ValueError("You need to give a name.")
    except:
        print("Your username was blank - try again!")
    else:
        print(f"Hello {user_name}")
        break


class NumberGuessGameError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def method_one(self, arg1 = "", arg2 = "") -> str:
        return True


while True:
    # How to handle if the string is empty?
    user_name = input("What is your username? ")

    try:
        if not user_name:
            error1 =  NumberGuessGameError("You need to give a name.")
            error1.method_one()
        if user_name == "Error":
            raise Exception()
    except NumberGuessGameError as exp:
        print(exp)
    except Exception as e:
        print("Something unexpected has happened.")
        raise e
    else:
        print(f"Hello {user_name}")
        break
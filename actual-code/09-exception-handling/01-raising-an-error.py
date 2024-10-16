import traceback

def run_calculation(number):
    return 10 / number

while True:
    try:
        user_input = input("What would you like to divide 10 by?")
    except:
        print("Problem getting input from user.")

    try:
        user_input = int(user_input)

    except Exception as e:
        print("Problem converting user input - was it definitely numbers?")
        print(e)
        print(traceback.format_exc())

    try:
        print(run_calculation(int(user_input)))
        raise ValueError("I")
    except TypeError as exp:
        print("You (or I) have used a variable with the wrong type.")
        print(exp)
    except ValueError:
        print("You can only enter numbers - not letters or other characters.")
    except ZeroDivisionError as exp:
        print("Don't be silly - you can't divide by zero!")
        raise exp
    except Exception as exp:
        print("Something unexpected has happened.")
        raise exp
    else:
        print("The dangerous code ran with no errors.")
    finally:
        print("This will run last whether the code was successful or not.")
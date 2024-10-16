def try_again(number):
    try:
        print(10 / number)


    except:
        print("I think you meant to do 10 / 5")
        try_again(5)

try_again(0)
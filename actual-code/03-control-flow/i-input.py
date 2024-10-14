
result = None
if input("True or false? ") == "True":
    result = True
else:
    result = False

print(result)

# Walrus Operator

user_input = input("Enter a word or press enter to quit")

while user_input != "":
    print(f"You entered {user_input}")
    user_input = input("Enter a word or press enter to quit")

print("Goodbye! All done!")

while (user_input2 := input("Enter a word or press enter to quit")) != "":
    print(f"You entered {user_input2}")

print("Goodbye")
print(user_input2)












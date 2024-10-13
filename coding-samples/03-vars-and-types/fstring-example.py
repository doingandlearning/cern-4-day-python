# Example of using f-strings - introduced in Python 3.6
name = "Adam"
age = 22

message = f"Hello {name}, you are {age}"
print(message)

welcome = 'Hello'
message = f'The value of 2 + 3 is: {2 + 3}, the len of {welcome} is {len(welcome)}'
print(message)

# printing a floating point number
a = 10.1234
message = f'Result: {a:.2f}'
print(message)

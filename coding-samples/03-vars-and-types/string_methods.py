# String replacement / substitution
welcome_message = 'Hello World!'
print(welcome_message.replace("Hello", "Goodbye"))

# Generating multiple strings
print('*' * 10)
print('Hi' * 10)

# Testing strings containing another string
print('Edward Alan Rawlings'.find('Alan'))
print('Edward John Rawlings'.find('Alan'))

print('James' == 'James')  # prints True
print('James' == 'John')  # prints False
print('James' != 'John')  # prints True
print('James' == 'james')  # prints False

# Various different string operations
some_string = 'Hello World'
print('Testing a String')
print('-' * 20)
print('some_string', some_string)
print("some_string.startswith('H')", some_string.startswith('H'))
print("some_string.startswith('h')", some_string.startswith('h'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())

# String conversions
print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', "   xyz   ".strip())

# Adding a number to a string - need to use the str() function
msg = 'Hello Lloyd you are ' + str(21)
print(msg)

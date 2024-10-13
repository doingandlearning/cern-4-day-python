# Defining strings

my_variable = 'Bob'
print(my_variable)
my_variable = "Eloise"
print(my_variable)

# A multi line string
my_variable = """
Hello
  World
"""
print(my_variable)

# Embedding strings
print("It's the day")
print('She said "hello" to everyone')

# Concatenating Strings
string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
print(string_3)
print(len(string_3))

# Calculating the length of a string
my_string = 'Hello World'
print(len(my_string))

# Can Obtain substring
my_string = 'Hello World'
print(my_string[4])
print(my_string[1:5])
print(my_string[:5])
print(my_string[2:])

# String methods adding in Python 3.9
info = '-John Hunt*'
print(info)
print(info.removeprefix('-'))
print(info.removesuffix('*'))








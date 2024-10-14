print("Hello world!")

# user_name = input("What is your name? ")
#
# print("Hello " + user_name + ", how are you today?")
print(f"Hello {1 + 1}, how are you today?")
print("Hello " + str(1)+ str(1))
# print("Hello $1, how are you today?".format())
is_completed = True
is_completed = False
print(type(is_completed))
is_completed = 'Not yet'
print(type(is_completed))

triple_quotes = """Longer text
    which has new lines
        which will be recognised when we print.
"""
print(triple_quotes)

triple_quotes.upper()
print(triple_quotes.upper())
print(len(triple_quotes))

my_name: str = "Kevin"
my_name = 3

triple_quotes.startswith("Hello") # True/
finish = 10
print(triple_quotes[4])
print(triple_quotes[4:10])
print(triple_quotes[4:finish:2])
print(triple_quotes[:10])
print(triple_quotes[::2])
print(triple_quotes[:-2])
print(triple_quotes[::-1])
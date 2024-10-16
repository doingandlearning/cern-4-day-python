"""
This is a very useful utility library.
"""



def printer(message):
    print("I'm about to print.")
    print(message)
    print("I just printed.")

class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Shape called {self.name}"

default_shape = Shape("rhombus")

if __name__ == "__main__":
    print("I am the utils module!")
    print(__name__)
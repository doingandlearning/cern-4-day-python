def some_meaningful_name(param1, param2):
    """
    This is a meaningful function that does something meaningful
    :param param1: The first parameter
    :param param2: The second parameter
    :return String concat of hte parameters, a boolean, an int
    """
    print("Hello!")
    print(f"The first parameter was {param1} and the second was {param2}.")
    return param1 + param2, True, 17
concat, boolResult, intResult = some_meaningful_name("CERN", "Meyrin")
print(concat)

# Unpack Tuple


firstVariable, secondVariable, thirdVariable = ("first", "second", "third")

print(firstVariable)
print(secondVariable)
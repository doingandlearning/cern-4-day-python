# Provides examples of using the Python array module
# to hold an ordered, mutable, indexed sequence of values
# Note in many examples the term list and array is used
# interchangeably in Python, but Python arrays are not lists
# They are less flexible but are more space efficient and can be faster
# Python arrays specify the type of value held in the array
# i - int, l - long, d - double, f - float, u - unicode char
# This can be important if you need to share an array with C code

# Import the Python array module
import array as arr

# Create an array of double/float type.
# The letter d is a type code which determines
# the type of the array during creation
print('Creating an array of doubles')
data = arr.array('d', [1.1, 3.5, 4.5])
print('data:', data)

# Creating an array of integers
data = arr.array('i', [1, 2, 5, 6, 9])
print('data:', data)

# Use indices to access elements of array
# Note index starts from 0 (not 1)
print("First element:", data[0])
print("Second element:", data[1])
print("Last element:", data[-1])

# Can obtain a sub array
print('data[2:4]:', data[2:4])  # 3rd to 4th

# Change a value at an index
# changing first element
data[2] = 0
print('Updated data:', data)

# Can remove array elements
del data[2]  # removing third element
print('Data after removal:', data)

# Can concatenate arrays
odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])
# Concatenate the two arrays together
numbers = odd + even

print(numbers)
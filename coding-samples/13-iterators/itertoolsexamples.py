import itertools

# Create iterable with element repeated specified number of
#  times (possibly infinite)
r2 = list(itertools.repeat("hello", 5))
print(r2)

# Connect two iterables together
r1 = list(itertools.chain([1, 2, 3], [2, 3, 4]))
print(r1)

values = [1, 3, 5, 7, 9, 3, 1]

# Create iterable with elements from supplied iterator between
#  the two indexes (use ”None” for second index to go to end)
r4 = list(itertools.islice(values, 3, 6))
print(r4)

# Create iterable with elements from first iterator starting
#  where predicate function fails
r3 = list(itertools.dropwhile(lambda x: x < 5, values))
print(r3)

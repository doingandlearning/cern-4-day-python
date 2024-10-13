# Working with Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed
print(len(basket))

for item in basket:
    print(item, ',', sep='', end='')

print()
print('apple' in basket)

basket.remove('apple')  # raises an error if not present
basket.discard('apricot')
print(basket)

basket.add('apricot')
print(basket)

basket = {'apple', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)

basket.clear()
print(basket)

s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}

print('Union:', s1 | s2)
print('Union method: ', s1.union(s2))

print('Intersection:', s1 & s2)
print('Intersection method: ', s1.intersection(s2))

print('Difference:', s1 - s2)
print('Difference method: ', s1.difference(s2))

# returns all the items present in given sets, except the items in their intersections
print('Symmetric Difference:', s1 ^ s2)
print('Symmetric diff method: ', s1.symmetric_difference(s2))

s1 = {(1, 2, 3)}
print(s1)

# Need to convert sets  into frozensets
s2 = {frozenset({1, 2, 3})}
print(s2)

# Convert lists into a tuple
list1 = [55, 60, 43, 55, 65]
results_set = {tuple(list1), 'John', 'CS110'}
print(f'results_set: {results_set}')

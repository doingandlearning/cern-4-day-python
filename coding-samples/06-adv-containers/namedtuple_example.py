from collections import namedtuple

# Creates a new tuple subclass called Person
Person = namedtuple('Person', ['age', 'gender', 'name'])

# Can use new subclass to create tuple-like objects
row1 = Person(age=25, gender='male', name='Gryff')
print(row1.age)
print(row1[0])
for item in row1:
    print(item)

row2 = Person(age=25, gender='female', name='Phoebe')
print(row2.name)

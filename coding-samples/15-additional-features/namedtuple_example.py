from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'degree'])

# Adding values
undergrad_student = Student('John', '21', 'Computer Science')
postgrad = Student(name='Denise', age=25, degree='PhD')

print(undergrad_student)
print(postgrad)

# Access using index
print(f'Name via index (student[0]): {undergrad_student[0]}')

# Access using name
print(f'Name via named member (student.name): {undergrad_student.name}')

# Can find out the field names using _fields
print(undergrad_student._fields)

for value in undergrad_student:
    print(value)

# Invalid cos its a tuple
# postgrad.name = "Pete"
# print(postgrad)

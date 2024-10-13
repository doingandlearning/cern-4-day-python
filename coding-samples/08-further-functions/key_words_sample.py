def my_function(*args, **kwargs):
    for arg in args:
        print('arg:', arg)

    for key in kwargs.keys():
        print('key:', key, 'has value: ', kwargs[key])


my_function('John', 'Denise',
            daughter='Phoebe', son='Adam')

print('-' * 50)

my_function('Paul', 'Fiona',
            son_number_one='Andrew',
            son_number_two='James',
            daughter='Joselyn')

def other_func(**kwargs):
    for key in kwargs.keys():
        print('key:', key, 'has value: ', kwargs[key])

other_func(name='John', age = 21)

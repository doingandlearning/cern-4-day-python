
def prime_number_generator(num):
    """ Provides a sequence of prime numbers up to num"""
    for i in range(2, num):
        # Assume a number is a prime number until proved otherwise
        prime_number = True
        for j in range(2, i):
            # If there is no remainder then its not a prime number
            if i % j == 0:
                prime_number = False
                break
        if prime_number:
            yield i


number = input('Please input the number:')
if number.isnumeric():
    num = int(number)
    if num <= 2:
        print('Number must be greater than 2')
    else:
        for prime in prime_number_generator(num):
            print(prime, end=', ')
else:
    print('Must be a positive integer')

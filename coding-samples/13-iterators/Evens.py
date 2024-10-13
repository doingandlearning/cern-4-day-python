class Evens(object):
    """ Illustrates a class implementing the
     Iterable and Iterator protocols """

    def __init__(self, limit):
        self.limit = limit
        self.val = 0

    # Makes this class Iterable
    def __iter__(self):
        return self

    # Makes this class an Iterator
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration
        else:
            return_val = self.val
            self.val += 2
            return return_val


print('Start')
for i in Evens(6):
    print(i, end=', ')

print('Done')





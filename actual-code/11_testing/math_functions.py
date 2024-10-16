def add(a,b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Must only pass numbers")
    return a + b

def subtract(a,b):
    return a - b
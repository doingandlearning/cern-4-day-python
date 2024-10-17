class Quantity:
    def __init__(self, initial = 0):
        self.value = initial

    def __str__(self):
        return f"Quantity of value {self.value}"

    def add(self, other):
        if type(other) is not Quantity:
            raise TypeError("You can only add Quantity to Quantity")
        new_value = self.value + other.value
        return Quantity(new_value)

    def __add__(self, other):
        if type(other) is not Quantity:
            raise TypeError("You can only add Quantity to Quantity")
        new_value = self.value + other.value
        return Quantity(new_value)



q1 = Quantity(5)
q2 = Quantity(10)

q3 = q1.add(q2)
# q1.add(7)
q3 = q1 + q2
print(q1)
print(q2)
print(q3)
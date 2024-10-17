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

    def __mul__(self, other):
        if type(other) is not int:
            raise TypeError("Can only multiply Quantity by int")
        return Quantity(self.value * other)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value >= other.value


q1 = Quantity(5)
q2 = Quantity(10)
print(q2 < q1) # False
print(q1 < q2) # True
print(q1 > q2)
print(q1 == q2)
print(q1 == q1)
q5 = Quantity(5)
print(q1 == q5)
print(q1 >= q5)
print(q1 <= q5)
q3 = q1.add(q2)
q4 = q1 * 7 + Quantity(10) # Quantity(35)

# q1.add(7)
q3 = q1 + q2
print(q1)
print(q2)
print(q3)
print(q4)
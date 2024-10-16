from math_functions import add, subtract
import pytest

@pytest.mark.parametrize(
    'number1, number2, expected_output', [
        (1,1,2),
        (-4, -2, -6),
        (0, 5, 5),
        (0.1, 0.1, 0.2)
    ]
)
def test_adding_two_numbers_add_together(number1, number2, expected_output):
    # Arrange   /   Given
    # Act       /   When
    result = add(number1, number2)

    # Assert    /   Then
    assert result == expected_output

def test_fails_if_adding_none_numbers():
    # Arrange   /   Given
    number1 = []
    number2 = {}

    # Assert    /   Then
    with pytest.raises(TypeError):
    # Act       /   When
        result = add(number1, number2)

def test_fails_if_adding_two_strings():
    num1 = "one"
    num2 = "two"

    with pytest.raises(TypeError):
        add(num1, num2)

def test_fails_if_adding_two_lists():
    num1 = [1,2,3]
    num2 = [3,4,5]

    with pytest.raises(TypeError):
        add(num1, num2)




@pytest.mark.parametrize("a,b,result", [
    (1,1,0),
    (-1,-1, 0),
    (7, -1, 8),
    (-1, 7, -8)
])
def test_subtracting_integers(a,b, result):
    assert subtract(a,b) == result

@pytest.mark.parametrize("a,b,result", [
    (1.2,1.2,0),
    (-1.2,-1.2, 0),
    (7.1, -1.1, 8.2),
    (-1.1, 7.1, -8.2),
    (0.3, 0.2, pytest.approx(0.1))
])
def test_subtracting_floats(a,b, result):
    assert subtract(a,b) == result
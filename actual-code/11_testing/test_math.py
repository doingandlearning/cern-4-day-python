from math_functions import add
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






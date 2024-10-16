### Function for Practice

You can add this function to your `math_functions.py` file to give students more practice with testing:

```python
def subtract(number1, number2):
    return number1 - number2
```

### Lab for Practice

1. **Add Subtraction Tests**:
   Write unit tests for a new function `subtract(number1, number2)`, similar to how you tested the `add` function.

2. **Write Parametrized Tests**:
   Create parametrized tests that cover different cases like positive numbers, negative numbers, and floats.

3. **Error Handling**:
   Write tests to ensure the function raises appropriate errors (e.g., `TypeError`) when incorrect types (like strings, lists, etc.) are passed to the `subtract` function.

Here’s the outline for the lab task:

### Lab Instructions

1. **Create a new function:**
   - Write a function `subtract(number1, number2)` inside `math_functions.py`. This function should return the result of subtracting `number2` from `number1`.

2. **Test Cases**:
   - Implement tests for your subtraction function. Follow the pattern from the lab 
   - Parametrized test to check correct subtraction
   - Write tests to check if `subtract` raises `TypeError` when inputs are invalid:
   

3. **Run Your Tests**:
   Use `pytest` to run your tests and verify they pass.

### Bonus Challenge:

- Extend your tests to cover edge cases like subtracting very large or very small numbers.

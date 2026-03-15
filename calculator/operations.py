"""
Arithmetic operations module.

Best practices demonstrated here:
- Each function has a single, well-defined responsibility.
- Functions are named with clear verbs describing what they do.
- Type hints make the expected inputs and outputs explicit.
- Docstrings document purpose, parameters, return values, and exceptions.
- Edge cases (e.g., division by zero) are handled with informative errors.
"""


def add(first_number: float, second_number: float) -> float:
    """Return the sum of two numbers.

    Args:
        first_number: The first operand.
        second_number: The second operand.

    Returns:
        The arithmetic sum of first_number and second_number.

    Examples:
        >>> add(3, 4)
        7
        >>> add(-1, 1)
        0
    """
    return first_number + second_number


def subtract(first_number: float, second_number: float) -> float:
    """Return the difference of two numbers.

    Args:
        first_number: The number to subtract from.
        second_number: The number to subtract.

    Returns:
        The result of first_number minus second_number.

    Examples:
        >>> subtract(10, 3)
        7
        >>> subtract(0, 5)
        -5
    """
    return first_number - second_number


def multiply(first_number: float, second_number: float) -> float:
    """Return the product of two numbers.

    Args:
        first_number: The first factor.
        second_number: The second factor.

    Returns:
        The arithmetic product of first_number and second_number.

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-2, 5)
        -10
    """
    return first_number * second_number


def divide(dividend: float, divisor: float) -> float:
    """Return the quotient of two numbers.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        The result of dividing dividend by divisor.

    Raises:
        ValueError: If divisor is zero, since division by zero is undefined.

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return dividend / divisor

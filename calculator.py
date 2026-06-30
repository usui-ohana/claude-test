def add(a, b):
    """Return the sum of a and b.

    Args:
        a: First addend.
        b: Second addend.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """Return the difference of a and b.

    Args:
        a: Value to subtract from.
        b: Value to subtract.

    Returns:
        The result of a - b.
    """
    return a - b


def multiply(a, b):
    """Return the product of a and b.

    Args:
        a: First factor.
        b: Second factor.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("division by zero is not allowed")
    return a / b


def power(a, b):
    """Return a raised to the power of b.

    Args:
        a: The base.
        b: The exponent.

    Returns:
        The result of a ** b.

    Raises:
        ValueError: If a is zero and b is negative.
    """
    if a == 0 and b < 0:
        raise ValueError("zero cannot be raised to a negative power")
    return a ** b


if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 1))
    print(multiply(4, 6))
    print(divide(10, 2))
    print(power(2, 3))

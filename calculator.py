def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


if __name__ == "__main__":
    a, b = 10, 3
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b):.4f}")
    print(f"{a} ^ {b} = {power(a, b)}")

    print("\nDivision by zero:")
    try:
        divide(a, 0)
    except ValueError as e:
        print(f"  Error: {e}")

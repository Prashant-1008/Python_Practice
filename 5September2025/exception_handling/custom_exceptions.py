class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed."""


def sqrt_non_negative(x: float) -> float:
    if x < 0:
        raise NegativeNumberError("x must be non-negative")
    # Simple Newton method for demonstration
    guess = x if x > 1 else 1.0
    for _ in range(20):
        guess = 0.5 * (guess + x / guess)
    return guess


if __name__ == "__main__":
    print(sqrt_non_negative(9))
    try:
        print(sqrt_non_negative(-1))
    except NegativeNumberError as exc:
        print("Caught:", exc) 
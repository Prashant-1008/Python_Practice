from mymath import add, subtract, multiply, divide
from string_utils import to_title_case, is_palindrome


def demo_modules() -> None:
    print("Math:")
    print("  add(2, 3) =", add(2, 3))
    print("  subtract(5, 2) =", subtract(5, 2))
    print("  multiply(3, 4) =", multiply(3, 4))
    try:
        print("  divide(10, 2) =", divide(10, 2))
        print("  divide(1, 0) -> should raise")
        divide(1, 0)
    except ZeroDivisionError as exc:
        print("  caught:", exc)

    print("\nStrings:")
    print("  to_title_case('hello world') =", to_title_case('hello world'))
    for text in ["Level", "hello", "Madam, I'm Adam!"]:
        print(f"  is_palindrome({text!r}) =", is_palindrome(text))


if __name__ == "__main__":
    demo_modules() 
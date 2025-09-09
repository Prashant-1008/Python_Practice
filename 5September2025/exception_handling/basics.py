def parse_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        print("ValueError:", exc)
        raise
    else:
        print("Parsed successfully")
        return number
    finally:
        print("Finished parse attempt")


if __name__ == "__main__":
    for s in ["42", "-7", "hello"]:
        try:
            print("Input:", s, "->", parse_int(s))
        except Exception:
            print("Failed to parse", s) 
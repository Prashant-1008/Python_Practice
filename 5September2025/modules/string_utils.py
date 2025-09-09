def to_title_case(text: str) -> str:
    return text.title()


def is_palindrome(text: str) -> bool:
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1] 
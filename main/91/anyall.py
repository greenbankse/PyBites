VOWELS = "aeiou"
PYTHON = "python"
DIGITS = "0123456789"


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
    VOWELS. Match is case insensitive."""

    return len(set(input_str.lower()).difference(VOWELS)) == 0


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
    chars are in it. Match is case insensitive."""
    return len(set(input_str.lower()).intersection(PYTHON)) > 0


def contains_digits(input_str):
    """Receives input string and checks if it contains
    one or more digits."""
    return len(set(input_str.lower()).intersection(DIGITS)) > 0

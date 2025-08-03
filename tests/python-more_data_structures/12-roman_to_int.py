#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): Roman numeral string.

    Returns:
        int: The integer value of the Roman numeral.
             Returns 0 if input is not a string or is None.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

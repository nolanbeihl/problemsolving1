
number_check = input('Can you find a happy number?: ' )

from problemsolving2 import number_check


def pdi_function(number, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total += pow(number % base, 2)
        number = number // base
    return total

def is_happy(number: int) -> bool:
    """Determine if the specified number is a happy number."""
    seen_numbers = set()
    while number > 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = pdi_function(number)
    return number == 1

is_happy(int(number_check))






"""Utility functions for the demo app."""


def calculate_percentage(value: int, total: str = 100) -> float:
    """This function represents an invalid docstring according to our configuration"""
    try:
        return (value / total) * 100
    except ZeroDivisionError:
        return 0

def should_be_a_dict_comprehension():
    pairs = (("a", 1), ("b", 2))
    result = {}
    for x, y in pairs:
        result[x] = y

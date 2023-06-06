"""Utility functions for the demo app."""


def calculate_percentage(value: int, total: str = 100) -> float:
    """This function represents an invalid docstring according to our configuration"""
    try:
        return (value / total) * 100
    except ZeroDivisionError:
        return 0

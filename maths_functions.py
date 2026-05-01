"""Basic maths functions project.

This module provides common arithmetic helpers with input validation.
"""

from __future__ import annotations

from math import sqrt


Number = int | float


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the subtraction of two numbers."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the multiplication of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a: Number, b: Number) -> Number:
    """Return the remainder after division.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot modulus by zero.")
    return a % b


def power(base: Number, exponent: Number) -> Number:
    """Return base raised to exponent."""
    return base**exponent


def square(value: Number) -> Number:
    """Return value squared."""
    return value * value


def cube(value: Number) -> Number:
    """Return value cubed."""
    return value * value * value


def absolute(value: Number) -> Number:
    """Return absolute value."""
    return abs(value)


def average(*values: Number) -> float:
    """Return average of one or more numbers.

    Raises:
        ValueError: If no values were provided.
    """
    if not values:
        raise ValueError("At least one value is required.")
    return sum(values) / len(values)


def percentage(part: Number, whole: Number) -> float:
    """Return percentage represented by ``part`` out of ``whole``.

    Raises:
        ZeroDivisionError: If ``whole`` is zero.
    """
    if whole == 0:
        raise ZeroDivisionError("Whole cannot be zero when calculating percentage.")
    return (part / whole) * 100


def factorial(n: int) -> int:
    """Return factorial of a non-negative integer.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def is_even(n: int) -> bool:
    """Return True if number is even."""
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Return True if number is odd."""
    return n % 2 != 0


def root(value: Number, degree: Number = 2) -> float:
    """Return the nth root of value.

    Raises:
        ValueError: If degree is zero or if an even root of a negative number is requested.
    """
    if degree == 0:
        raise ValueError("Root degree cannot be zero.")
    if value < 0 and degree % 2 == 0:
        raise ValueError("Cannot take an even root of a negative number in real numbers.")

    if degree == 2:
        return sqrt(value)
    return value ** (1 / degree)

#!/usr/bin/env python3

"""
This module provides two functions: dec_to_b30 and b30_to_dec

The purpose of those functions is to convert between regular decimal
numbers and a version of a base30 system that excludes vowels and other 
letters than may be mistaken for numerals. This is useful for encoding large
numbers in a more compact format while reducing the likelihood of errors
while typing the base30-encoded version.

The base30 digits include 0-9 and the letters BCDFGHJKLMNPQRSTVWXZ
"""


class Error(Exception):
    """Base class for other exceptions"""

    pass


class NumberInputError(Error):
    """Raised when the input value is a float"""

    pass


class ImproperBase30FormatError(Error):
    """Raised when the input value contains letters that aren't allowed in the base30 specification"""

    pass


values = "0123456789BCDFGHJKLMNPQRSTVWXZ"
digit_value_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "B": 10,
    "C": 11,
    "D": 12,
    "F": 13,
    "G": 14,
    "H": 15,
    "J": 16,
    "K": 17,
    "L": 18,
    "M": 19,
    "N": 20,
    "P": 21,
    "Q": 22,
    "R": 23,
    "S": 24,
    "T": 25,
    "V": 26,
    "W": 27,
    "X": 28,
    "Z": 29,
}


def dec_to_b30(num):
    """Given a decimal number, return the base30-encoded equivalent."""
    base_num = ""

    # Make sure the function received an integer as input
    try:
        if isinstance(num, float):
            raise NumberInputError
        num = int(num)
    except (ValueError, NumberInputError):
        print("Must provide an integer to convert.")
    else:
        while num > 0:
            digit = int(num % 30)
            if digit < 10:
                base_num += str(digit)
            else:
                base_num += values[digit]
            num //= 30
        base_num = base_num[::-1]
        return base_num


def b30_to_dec(num):
    """Given a base30-encoded number, return the decimal equivalent."""

    # Make sure the function received a base30 number that doesn't include any illegal characters
    try:
        num = str(num)
        for c in num:
            if c not in values:
                raise ImproperBase30FormatError
    except ImproperBase30FormatError:
        print(f"Invalid base30 format. My only contain {values}.")
    else:
        dec_num = 0
        rev_num = num[::-1]
        for i in range(len(rev_num)):
            dec_num += digit_value_dict[rev_num[i]] * (30 ** i)
        return dec_num

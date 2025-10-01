# arvd_ap/__init__.py

"""
This module provides a collection of utility functions for numerical and string operations.
Functions included:
    - avg(): Calculates the average of a list of numbers.
    - sign(): Determines the sign (positive, negative, zero) of a number.
    - perfect_num(): Checks if a number is a perfect number.
    - armstrong_num(): Checks if a number is an Armstrong number.
    - palindrome_num(): Checks if a number is a palindrome.
    - primality(): Checks if a number is prime.
    - fib(): Generates Fibonacci numbers.
    - vowel_count(): Counts the number of vowels in a string.
    - consonant_count(): Counts the number of consonants in a string.
    - space_count(): Counts the number of spaces in a string.
    - palindrome_str(): Checks if a string is a palindrome.
    - word_count(): Counts the number of words in a string.
    - alpha_count(): Counts the number of alphabetic characters in a string.
    - int_count(): Counts the number of integer digits in a string.
    - div_it(): Divides two numbers and returns the result.
    - tell_it(): Provides information or description about a given input.
"""

from .arvd_ap import *

__all__ = [
    'avg()', 'sign()', 'perfect_num()', 'armstrong_num()', 'palindrome_num()',
    'primality()', 'fib()', 'vowel_count()', 'consonant_count()', 'space_count()',
    'palindrome_str()', 'word_count()', 'alpha_count()', 'int_count()', 'div_it()', 'tell_it()'
]

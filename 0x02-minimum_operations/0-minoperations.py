#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Returns number of the fewest iterations possible"""
    if n <= 1:
        return 0
    mod = 2
    iterations = 0
    while n > 1:
        if n % mod == 0:
            iterations = iterations+mod
            n = n/mod
        else:
            mod = mod + 1
    return iterations

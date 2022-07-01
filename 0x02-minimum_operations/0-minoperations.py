#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result in exactly
 n H characters in the file
"""

def minOperations(n):
    """Calculate fewest no. of operations needed to result in n H characters"""
    i = 0
    m = 2
    while n > 1:
        while not n % m:
            i += m
            n /= m
        m += 1
    return i

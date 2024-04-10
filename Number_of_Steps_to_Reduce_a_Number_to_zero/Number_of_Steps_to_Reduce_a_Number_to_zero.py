# 1342. Number of Steps to Reduce a Number to zero

"""
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise,
you have to subtract 1 from it.

Constraints:
1)0 <= num <= 10**6
"""


def numberOfSteps(num: int) -> int:
    x = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        x += 1
    return x

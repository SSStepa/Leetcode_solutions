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


# leetcode examples, the smallest and the largest:
values = [
    {"input": 1, "output": 1},
    {"input": 14, "output": 6},
    {"input": 8, "output": 4},
    {"input": 123, "output": 12},
    {"input": 10 ** 6, "output": 26},
]


def test_1342(testcases=values):
    for testcase in testcases:
        if numberOfSteps(testcase["input"]) != testcase["output"]:
            raise Exception("Wrong answer in: ", testcase)

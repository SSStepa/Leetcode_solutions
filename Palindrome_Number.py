# 9. Palindrome Number

"""

 Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Constraints:
1) -2**31 <= x <= 2**31 - 1
"""


def isPalindrome(x: int) -> bool:
    our_list = list(str(x))
    y = -1
    for i in our_list:
        if i == our_list[y]:
            y -= 1
            continue
        else:
            return False
    return True


# leetcode examples, the smallest and the largest:
values = [
    {"input": 121, "output": True},
    {"input": -121, "output": False},
    {"input": 10, "output": False},
    {"input": -2 ** 31, "output": False},
    {"input": (2 ** 31 - 1), "output": False},
]


def test_9(testcases=values):
    for testcase in testcases:
        if isPalindrome(testcase["input"]) != testcase["output"]:
            raise Exception("Wrong answer in: ", testcase)

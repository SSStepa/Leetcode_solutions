from random import randint

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


def test(testcase):
    if isPalindrome(testcase[0]) == testcase[1]:
        pass
    else:
        print("Wrong")


# leetcode examples, the smallest and the largest, 2 random numbers:
run = [
    (121, True),
    (-121, False),
    (10, False),
    (-2 ** 31, False),
    ((2 ** 31 - 1), False)
]
ex1 = str(randint(0, 10000))
ex1 += ex1[::-1]
run.append((int(ex1), True))
ex2 = str(randint(-1000, 1000))
if ex2[0] == ex2[-1]:
    ex2 += "0"
run.append((int(ex2), False))
for i in run:
    test(i)


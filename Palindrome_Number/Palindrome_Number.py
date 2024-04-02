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

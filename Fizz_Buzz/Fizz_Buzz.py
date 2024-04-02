# 412. Fizz Buzz

"""

Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Constraints:
1) 1 <= n <= 10**4
"""


def fizzBuzz(n: int) -> list[str]:
    our_list = [i for i in range(1, n + 1)]
    for i in our_list:
        if i % 3 == 0 and i % 5 == 0:
            our_list[our_list.index(i)] = "FizzBuzz"
        elif i % 3 == 0:
            our_list[our_list.index(i)] = "Fizz"
        elif i % 5 == 0:
            our_list[our_list.index(i)] = "Buzz"
        else:
            our_list[our_list.index(i)] = str(i)
    return our_list

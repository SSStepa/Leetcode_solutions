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


# leetcode examples:
values = [
    {"input": 3, "output": ["1", "2", "Fizz"]},
    {"input": 5, "output": ["1", "2", "Fizz", "4", "Buzz"]},
    {"input": 15, "output": ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]},
]


def test_412(testcases=values):
    for testcase in testcases:
        if fizzBuzz(testcase["input"]) != testcase["output"]:
            raise Exception("Wrong answer in:", testcase)

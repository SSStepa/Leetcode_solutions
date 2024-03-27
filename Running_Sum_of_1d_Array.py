# 1480. Running Sum of 1d Array

"""
Given an array nums. We define a running sum of an array
as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Constraints:

1) 1 <= nums.length <= 1000
2) -10**6 <= nums[i] <= 10**6
"""


def runningSum(self, nums: list[int]) -> list[int]:
    our_list = [nums[0]]
    y = 1
    element = our_list[-1]
    while y < len(nums):
        x = nums[y]
        our_list.append(x + element)
        y += 1
        element = our_list[-1]
    return our_list


# leetcode examples:
values = [
    {"input": [1, 2, 3, 4], "output": [1, 3, 6, 10]},
    {"input": [1, 1, 1, 1, 1], "output": [1, 2, 3, 4, 5]},
    {"input": [3, 1, 2, 10, 1], "output": [3, 4, 6, 16, 17]},
]


def test_1480(testcases=values):
    for testcase in testcases:
        if runningSum(testcase["input"]) != testcase["output"]:
            raise Exception("Wrong answer in:", testcase)

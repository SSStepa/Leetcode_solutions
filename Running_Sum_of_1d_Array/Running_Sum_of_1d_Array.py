# 1480. Running Sum of 1d Array

"""
Given an array nums. We define a running sum of an array
as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Constraints:

1) 1 <= nums.length <= 1000
2) -10**6 <= nums[i] <= 10**6
"""


def runningSum(nums: list[int]) -> list[int]:
    our_list = [nums[0]]
    y = 1
    element = our_list[-1]
    while y < len(nums):
        x = nums[y]
        our_list.append(x + element)
        y += 1
        element = our_list[-1]
    return our_list

# 628. Maximum Product of Three Numbers

"""
Given an integer array nums, find three numbers whose product
is maximum and return the maximum product.


Constraints:
3 <= nums.length <= 10**4
-1000 <= nums[i] <= 1000
"""


def maximumProduct(nums: list[int]) -> int:
    nums = sorted(nums)
    if nums[0] >= 0:
        y, z = -2, -3
    elif nums[0] < 0 <= nums[-1]:
        if nums[0] * nums[1] > nums[-2] * nums[-3]:
            y, z = 0, 1
        else:
            y, z = -2, -3
    else:
        y, z = -2, -3
    x = nums[-1] * nums[y] * nums[z]
    return x

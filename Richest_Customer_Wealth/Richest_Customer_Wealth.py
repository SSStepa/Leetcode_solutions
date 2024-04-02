# 1672. Richest Customer Wealth

"""
You are given an m x n integer grid accounts where accounts[i][j] is
the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.

Constraints:
1) m == accounts.length
2) n == accounts[i].length
3) 1 <= m, n <= 50
4) 1 <= accounts[i][j] <= 100
"""


def maximumWealth(accounts: list[list[int]]) -> int:
    x = 0
    for i in accounts:
        if sum(i) > x:
            x = sum(i)
    return x

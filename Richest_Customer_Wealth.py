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


def maximumWealth(self, accounts: list[list[int]]) -> int:
    x = 0
    for i in accounts:
        if sum(i) > x:
            x = sum(i)
    return x


# leetcode examples:
values = [
    {"input": [[1,2,3],[3,2,1]], "output": 6},
    {"input": [[1,5],[7,3],[3,5]], "output": 10},
    {"input": [[2,8,7],[7,1,3],[1,9,5]], "output": 17},
]


def test_1672(testcases=values):
    for testcase in testcases:
        if maximumWealth(testcase["input"]) != testcase["output"]:
            raise Exception("Wrong answer in: ", testcase)

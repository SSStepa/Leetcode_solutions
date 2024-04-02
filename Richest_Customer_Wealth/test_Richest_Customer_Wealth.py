from .Richest_Customer_Wealth import maximumWealth


def test(testcase_1, testcase_2, testcase_3):
    assert maximumWealth(testcase_1["input"]) == testcase_1["output"]
    assert maximumWealth(testcase_2["input"]) == testcase_2["output"]
    assert maximumWealth(testcase_3["input"]) == testcase_3["output"]

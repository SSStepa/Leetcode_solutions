from .Running_Sum_of_1d_Array import runningSum


def test(testcase_1, testcase_2, testcase_3):
    assert runningSum(testcase_1["input"]) == testcase_1["output"]
    assert runningSum(testcase_2["input"]) == testcase_2["output"]
    assert runningSum(testcase_3["input"]) == testcase_3["output"]
